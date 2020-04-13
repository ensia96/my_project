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
        return HttpResponse(status=200)

    def get(self, request):
        return JsonResponse({'comment':list(Comments.objects.values())}, status=200)