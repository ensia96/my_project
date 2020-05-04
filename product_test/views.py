import json

from django.http import JsonResponse,HttpResponse
from django.views import View
from django.db.models import Q

from .models import *

class FilterView(View):

    def get(self, request,category_name):

        product = Product.objects.filter(
            Q(category__name = category_name)| Q(group__name = category_name))

        return JsonResponse(
            {
                'filter' : {
                    'gender':list(
                        set([
                            gender['gender'] for gender in product.values('gender')]
                        ).difference(['남녀공용','유니섹스'])
                    ),
                    'color' : [
                        {'name':value[0], 'code':value[1]} for (key,value) in sorted(
                            {
                                color['id'] : (color['color_name'],color['color_code'])
                                for color in Color.objects.filter(product__in = product).values()
                            }.items())],
                    'size':[
                        size[1] for size in sorted(
                            {
                                size['id']:size['size']
                                for size in Size.objects.filter(product__in=product).values()
                            }.items())],
                    'silhouette':[
                        value for (key,value) in sorted(
                            {
                                silhouette['id']:silhouette['name']
                                for silhouette in Silhouette.objects.filter(product__in=product).values()
                            }.items())]
                }
            }, status=200)

# ^ prefetch_related 로 한번에 호출 도전 + order_by 로 정렬

class ProductView(View):

    def get(self, request,category_name):

        products  = Product.objects.filter(
            Q(category__name = category_name)| Q(group__name = category_name)
        )

        sources      = products.prefetch_related('series_set','media_set','product_color')
        product_list = [
            product for product in products.filter(
                **{
                    (
                        key + '__in' if key == 'gender' else
                        'product_' + key + '__' + key + '_code__in' if key == 'color' else
                        'product_' + key + '__' + key + '__in' if key == 'size' else
                        key + '_id__name__in'
                    ) : (
                        request.GET.getlist(key) + ['남녀공용', '유니섹스']
                        if key == 'gender' else
                        request.GET.getlist('key')
                    )
                    for key in request.GET
                    if key in ['gender','color','size','silhouette']
                }
            ).values('id','code','name','price')][:30]

        try:

            for product in product_list:

                product['color_list'] = []

                for source in sources.get(code=product['code']).series_set.values('code'):

                    if '#' in source['code']:

                        source['code'] = source['code'].replace('#','')

                        image = sources.get(code=source['code']).media_set.values('media_url').first()['media_url']
                    if 'primary' not in image:
                        image = sources.get(code=source['code']).media_set.values('media_url')[1]['media_url']


                    product['color_list'].append({
                        'color_code' : sources.get(code=source['code']
                                                  ).product_color.values('color_code').first()['color_code'],
                        'image'      : image,
                        'hover'      : image.replace('primary','hover')
                    })

        except Product.DoesNotExist:

                image = sources.get(id=product['id']).media_set.values('media_url').first()['media_url']

                product['color_list'] = {
                    'color_code' : sources.get(id=product['id']
                                              ).product_color.values('color_code').first()['color_code'],
                    'image'      : image,
                    'hover'      : image.replace('primary','hover')}

        if product_list:
            return JsonResponse({'product' : product_list},status=200)
        return HttpResponse(status=404)
