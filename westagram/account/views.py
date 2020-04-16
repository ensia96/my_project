import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import User

from .utils import mk_token

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(name = data['name']).exists():
                return HttpResponse(status=400)
            User(
                name       = data['name'],
                password   = data['password'],
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)

class UserAuthView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(name = data['name']).exists():
                user = User.objects.get(name = data['name'])
                if user.password == data['password']:
                    token = mk_token(data['name'], data['password'])
                    return JsonResponse({'access-token':f'{token}'}, status=200)
                return HttpResponse(status=401)
            return HttpResponse(status=401)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)