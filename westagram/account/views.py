import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Users

class Signup(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Users.objects.get(name = data['name'])
            return HttpResponse(status=400)
        except Exception:
            Users(
                name       = data['name'],
                password   = data['password'],
            ).save()
            return HttpResponse(status=200)

class Signin(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            Users.objects.get(name = data['name'])
            user = Users.objects.get(name = data['name'])
            if user.password == data['password']:
                return HttpResponse(status=200)
            return HttpResponse(status=401)
        except Exception:
            return HttpResponse(status=401)