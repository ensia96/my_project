import bcrypt

from django.http import JsonResponse

def givetoken(inja): # 토큰발행 함수
    token = bcrypt.hashpw(inja.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') # 로그인에 성공하면 함수 호출
    return JsonResponse({'access-token':f'{token}'})

print(givetoken('akdrh1133'))