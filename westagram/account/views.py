import json, bcrypt, jwt

from django.http import HttpResponse, JsonResponse
from django.views import View

from .models import User
from westagram.settings import SECRET_KEY

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(name = data['name']).exists(): # 사용중인 아이디값이라면
                return HttpResponse(status=400)
            User(
                name       = data['name'],
                password   = bcrypt.hashpw(data['password'].encode('utf-8'),bcrypt.gensalt()).decode() # 암호를 저장할때는 받은 암호값을 인코딩하고, 솔팅을 얹어 해쉬를 한뒤, 디코드 한 상태로
            ).save()
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)

class UserAuthView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(name = data['name']).exists(): # DB 에 일치하는 아이디값이 있다면
                user = User.objects.get(name = data['name'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')): # 받은 암호값을 인코딩하고, DB 의 암호값을 디코드하여 비교
                    token = jwt.encode({'id':user.id}, SECRET_KEY, algorithm='HS256').decode('utf-8') # 프로젝트 고유 암호키와 HS256 암호화 방식으로 유저정보 토큰 생성
                    return JsonResponse({'access-token':token}, status=200) # 토큰 리턴
                return HttpResponse(status=401) # 암호가 일치하지 않음
            return HttpResponse(status=401) # ID 가 없음
        except KeyError:
            return JsonResponse({"message":"INVALID_KEYS"}, status=400)