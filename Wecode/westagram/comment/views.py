import json

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import Comment
from account.utils import need_permission

class ContentView(View):
    @need_permission
    def post(self, request):
        data = json.loads(request.body)
        Comment(
            name       = data['name'],
            content    = data['contents'],
        ).save()
        return HttpResponse(status=200)

    def get(self, request):
        user = request.GET.get('name', None)
        return JsonResponse({'comment':list(Comment.objects.filter(name = user).values())}, status=200)