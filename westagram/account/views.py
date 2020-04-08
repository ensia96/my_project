import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Users

class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        def createuser():
            Users(
                name       = data['name'],
                password   = data['password'],
            ).save()
        try:
            Users.objects.get(name = data['name'])
        except Exception:
            createuser()
            return JsonResponse({'message':'SUCCESS'}, status=200)
        else:
            return JsonResponse({'message':'ALREADY_EXIST'}, status=400)

class Signin(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Users.objects.get(name = data['name'])
        except Exception:
            return JsonResponse({'message':'INVALID_USER'}, status=401)
        else:
            user = Users.objects.get(name = data['name'])
            if user.password == data['password']:
                return JsonResponse({'message':'SUCCESS'}, status=200)
            else:
                return JsonResponse({'message':'INVALID_USER'}, status=401)