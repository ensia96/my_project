import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Comments

class Create(View):
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            name       = data['name'],
            contents   = data['contents'],
        ).save()

        return JsonResponse({'message':'SUCCESS'}, status=200)