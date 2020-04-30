import json

from django.http import JsonResponse,HttpResponse
from django.views import View

from .models import *

#Review.objects.create(rating=4,color_score=2,size_score=1,title='하하호호망고망고',comment='망고는 슈퍼개발자라구!',product=Product.objects.get(id=1),user=User.objects.get(name='춤망쓰')
# User.objects.create(email='mango@man.go',password='tbvjvkdnj1!!',name='춤망쓰',gender='망고',phone='010-5150-6992',birth='19000625')

class FilterView(View):
    def get(self, request,category_name):
        product = Product.objects.filter(category__name=category_name)
        product |= Product.objects.filter(group__name=category_name)
        return JsonResponse({
            'filter' :{
                'gender': list(
                    set([gen['gender'] for gen in product.values('gender')]).difference(['남녀공용','유니섹스'])
                ),
                'color' : [
                        {'name':value[0], 'code':value[1]} for (key,value) in sorted(
                            {
                                color['id'] : (color['color_name'],color['color_code'])
                                for color in Color.objects.filter(product__in = product).values()
                            }.items())],                'size':[
                    siz[1] for siz in sorted(
                        {
                            siz['id']:siz['size'
                               ] for siz in Size.objects.filter(
                                   product__in=product).values()
                        }.items())],
                'silhouette':[
                    value for (key,value) in sorted(
                        {
                            sil['id']:sil['name'
                               ] for sil in Silhouette.objects.filter(
                                   product__in=product).values()
                        }.items())]
            }
        }, status=200)

# ^ prefetch_related 로 한번에 호출 도전 + order_by 로 정렬

# unpacking, 필터안에 딕셔너리

class ProductView(View):
    def get(self, request,category_name):
        product = Product.objects.filter(category__name=category_name)
        product |= Product.objects.filter(group__name=category_name)
        filter_dict = {}
#            try refactory : else 없이는 동작 안함 / None 타입에선 필터기능 동작 안함
#            'gender__in': (request.GET.getlist('gender') if request.GET.getlist('gender') else None),
#            'product_color__color_code__in': (request.GET.getlist('color') if request.GET.getlist('color') else None),
#            'product_size__size': (request.GET.getlist('size') if request.GET.getlist('size') else None),
#            'silhouette__name': (request.GET.getlist('silhouette') if request.GET.getlist('silhouette') else None)
#        }

        if request.GET.getlist('gender', None):
            filter_dict['gender__in'] = request.GET.getlist('gender', None)+['남녀공용','유니섹스']
        if request.GET.getlist('color', None):
            filter_dict['product_color__color_code__in'] = request.GET.getlist('color', None)
        if request.GET.getlist('size', None):
            filter_dict['product_size__size'] = request.GET.getlist('size', None)
        if request.GET.getlist('silhouette', None):
            filter_dict['silhouette_id__name__in'] = request.GET.getlist('silhouette', None)
        source = product.prefetch_related('series_set','media_set','product_color')

        prod_list = [pro for pro in product.filter(**filter_dict).values('id','code','name','price')][:20]
        for prod in prod_list:
            try:
                prod['color_list']=[]
                for sou in source.get(code=prod['code']).series_set.values('code'):
                    if '#' in sou['code']:
                        sou['code'] = sou['code'].replace('#','')
                    prod['color_list'].append({
                        'color_code':source.get(code=sou['code']).product_color.values('color_code')[0]['color_code'],
                        'image':source.get(code=sou['code']).media_set.values('media_url')[0]['media_url'],
                        'hover':source.get(code=sou['code']).media_set.values('media_url')[0]['media_url'].replace('primary','hover')})
            except Product.DoesNotExist :
                prod['color_list']={
                    'color_code':source.get(id=prod['id']).product_color.values('color_code')[0]['color_code'],
                    'image':source.get(id=prod['id']).media_set.values('media_url')[0]['media_url'],
                    'hover':source.get(id=prod['id']).media_set.values('media_url')[0]['media_url'].replace('primary','hover')}
        return JsonResponse({'product':prod_list},status=200)
