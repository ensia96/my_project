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
            return JsonResponse({'message':'SUCCESS'}, status=200)
        try:
            Users.objects.get(name = data['name'])
            return JsonResponse({'message':'ALREADY_EXIST'}, status=400)
        except Exception:
            createuser()

class Signin(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Users.objects.get(name = data['name'])
            user = Users.objects.get(name = data['name'])
            if user.password == data['password']:
                return JsonResponse({'message':'SUCCESS'}, status=200)
            else:
                return JsonResponse({'message':'INVALID_USER'}, status=401)
        except Exception:
            return JsonResponse({'message':'INVALID_USER'}, status=401)