import jwt, json

from django.http import HttpResponse, JsonResponse

from .models import User
from westagram.settings import SECRET_KEY


def need_permission(func): # 함수를 인자로받는 데코레이터
    def check(self, request, *args, **kwargs): # def 상속받기위한 self, 데코레이팅 할 함수에 들어온 request
        if "Authorization" in request.headers: # request.headers 라는 str 형 data 에 토큰이 담긴 attribute 가 있는지
            token = request.headers["Authorization"] # 토큰이 담긴 attribute 에서 토큰정보를 추출해 변수에 담음
            try:
                user_id = jwt.decode(token.encode('utf-8'), SECRET_KEY, algorithm='HS256') # 디코딩한 데이터를 변수에 담음
                if User.objects.get(id=user_id['id']): # 토큰이 담고있는 유저정보가 DB에 있는지 판별
                    request.user = user_id
                    return func(self, request, *args, **kwargs) # 인증 완료 / 함수 실행
            except jwt.exceptions.DecodeError: # 디코딩 과정 에러 사용가능 토큰, 사용자 없음
                return HttpResponse(status=401) # 사용자가 없어 인증을 못하니 401
            except KeyError: # 여기서 키에러 필요한가?
                return JsonResponse({"message":"INVALID_KEYS"}, status=400)
        return HttpResponse(status=400) # 토큰이 없어 올바르지 않은 요청이니 400
    return check # 내부정의 함수 호출
