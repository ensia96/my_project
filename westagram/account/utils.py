import jwt


# encoded_jwt = jwt.encode({'some':'payload'}, 'akdrh1133', algorithm='HS256').decode('utf-8')
# decoded_jwt = jwt.decode(encoded_jwt, 'akdrh1133', algorithm='HS256')


# class Verify:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

def mk_token(name, password): # 토큰 발급
    return jwt.encode({'name':name}, password, algorithm='HS256').decode()

def vf_token(token, input_pw): # 토큰 검증
    return jwt.decode(token, input_pw, algorithm='HS256')