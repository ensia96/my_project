import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Comments

class Contents(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            name       = data['name'],
            contents   = data['contents'],
        ).save()

        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        data = json.loads(request.body)
        target = {'comment_list':list(Comments.objects.filter(name = data['name']).values('contents'))}
        if target == {'comment_list':[]} : 
            return JsonResponse({'message':'NO_DATA'}, status=400)
        return JsonResponse(target, status=200)