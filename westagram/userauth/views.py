import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account

class Sign_up(View):
    def post(self, request):
        data = json.loads(request.body)
        if Account.objects.get(name=data['name']):
            return JsonResponse({'Message':'ALREADY_EXIST'}, status=400) # already exist
        else :
            Account(
                name       = data['name'],
                password   = data['password']
            ).save()
            return JsonResponse(status=200) # welcome!

class Sign_in(View):
    def post(self, request):
        data = json.loads(request.body)
        if Account.objects.get(name=data['name']):
            userdata = Account.objects.get(name=data['name'])
            userpw   = userdata.password
            if userpw == data['password']:
                return JsonResponse({'Message':'SUCCESS'}, status=200) # user exist, pw match
                    # pw unmatch 는 많은 정보를 제공하기 때문에 보안을 위해 구현 x
        else:
            return JsonResponse({'Message':'INVALID_USER'}, status=401) # username unmatch