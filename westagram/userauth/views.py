import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Account

class Sign_up(View):
    def get(self, request):
        data = json.loads(request.body)
        if Account.objects.get(name=data['name']):
            return 0

    def post(self, request):
        if self.get(self, request) :
            Account(
                name       = get().data['name'],
                password   = get().data['password']
            ).save()
            return JsonResponse(status=200) # welcome!
        else :
            return JsonResponse({'Message':'ALREADY_EXIST'}, status=401) # already exist

class Sign_in(View):
    def get(self, request):
        data = json.loads(request.body)
        if Account.objects.get(name=data['name']):
            userdata = Account.objects.get(name=data['name'])
            userpw   = userdata.password
            if userpw == data['password']:
                return 1

    def post(self, request):
        if Sign_in.get(self, request):
            return JsonResponse({'Message':'SUCCESS'}, status=200) # user exist, pw match
                # pw unmatch 는 많은 정보를 제공하기 때문에 보안을 위해 구현 x
        else:
            return JsonResponse({'Message':'INVALID_USER'}, status=401) # username unmatch