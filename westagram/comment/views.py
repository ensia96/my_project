import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Comment

class Leave_comment(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            name       = data['name'],
            contents   = data['contents']
        ).save()
        return JsonResponse({"Message":"APPLIED"}, status=200)