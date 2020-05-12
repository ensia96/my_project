import os

import re

import mimetypes

from wsgiref.util import FileWrapper

from django.http.response import StreamingHttpResponse


range_re = re.compile(r'bytes\s*=\s*(\d+)\s*-\s*(\d*)', re.I)
# range_re 라는 변수는 정규표현식으로 컴파일화 한 정보
# re 모듈의 compile 이라는 메소드를 이용
# compile 함수 : 정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴
# re.I -> 대소문자를 구분하지 않고 매칭작업을 수행
# \s 는 띄어쓰기, \d 는 0~9 숫자
# 수량자 : + 는 1개 이상 / * 은 앞에 오는 값이 있을수도 없을수도
# f string 과 비슷한 string 을 다루는 방식 : r string 방식은 뒤에 오는 문자열에서 escaping 을 사용하지 않도록 함
# r string 을 사용한 이유는 뒤에 올 정규표현식을 위하여
# range_re 변수에 담기는 정보는 'bytes = (0~9 까지의 숫자가 있거나 없거나) - (0~9 까지의 숫자가 있거나 없거나) '
# range_re 변수에 담길 정보의 첫번째 숫자값 단위는 first_byte,
# ' - ' 뒤에 오는 두번째 숫자값 단위는 last_byte
# 원하는 정규표현식 컴파일 결과는 () 를 통해서 설정 가능!

class RangeFileWrapper(object):
    def __init__(self, filelike, blksize=8192, offset=0, length=None):
    # filelike = 클래스에 인자로 온 바이트화 된 파일 ( 패킷단위 )
    # blksize = 블록사이 ( 8192 는 8kb )
    # offset = 내부에서 사용할 변수 ( 0 을 기준으로 함 )
    # length = 길이라는 변수 ( None 값을 기준으로 함 )
        self.filelike = filelike
        self.filelike.seek(offset, os.SEEK_SET)
        # python 의 파일 개체에 대한 메소드는
        # 작업을 시작하는 open / 첫번째 인자로 대상, 두번째 인자로 처리방식, 세번째 인자로 포맷팅 등의 속성
        # 작업위치를 정하는 seek / 첫번째 인자로 이동값, 두번째 인자로 위치
        # 작업위치를 확인하는 tell
        # SEEK_SET 메소드는 파일 작업위치의 처음값 ( 0 과 같음 )
        self.remaining = length
        self.blksize = blksize

    def close(self):
    # 닫기 속성
        if hasattr(self.filelike, 'close'):
        # self.filelike 라는 개체가 close 라는 attribute 를 가졌는지 hasattr 메소드로 판별
            self.filelike.close()
            # true 라면 self.filelike 를 닫음

    def __iter__(self):
    # self ( 클래스 객체 ) 에 반복에 대한 속성을 부여
        return self

    def __next__(self):
    # 반복을 진행하도록 하는 속성을 부여 ( 다음 )
        if self.remaining is None:
        # If remaining is None, we're reading the entire file.
            data = self.filelike.read(self.blksize)
            # 8byte 로 읽은 정보 ( self.filelike ) 를 data 변수에 할당
            if data:
            # data 가 None 이 아니라면
                return data
                # data 를 return
            raise StopIteration()
            # else 라면 반복중지
        else:
        # self.remaining 의 값이 있다면
            if self.remaining <= 0:
            # self.remaining 이 0 보다 작거나 같다면
                raise StopIteration()
                # 반복중지
            data = self.filelike.read(min(self.remaining, self.blksize))
            # 
            if not data:
                raise StopIteration()
            self.remaining -= len(data)
            return data


def stream_video(request, path):
    range_header = request.META.get('HTTP_RANGE', '').strip()
    # range_header 변수는 사용자의 요청에 대한 META 데이터 ( 헤더 ) 에서 HTTP_RANGE 라는 정보
    # HTTP_RANGE 라는 변수 없을경우 '' 로 처리
    # strip 으로 여백 제거
    range_match = range_re.match(range_header)
    # range_match 변수는 위에서 받은 range_header 라는 변수에 대한 정규표현식처리가 된 데이터
    # 정규식 객체로써 할당되어있음
    size = os.path.getsize(path)
    # size 변수는 요청으로 받은 path 값을 os 객체의 path 메소드에서 getsize 함수를 이용하여 size 를 바이트화한 것
    content_type, encoding = mimetypes.guess_type(path)
    # mimetypes 라는 모듈의 guess_type 메소드를 이용하여 요청으로 받은 path 값의 파일유형과 인코딩유형을
    # 각각 content_type 변수와 encoding 변수에 할당
    content_type = content_type or 'application/octet-stream'
    # content_type 이 None 일 경우 예외처리를 위한 값 할당
    # https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    if range_match:
    # httprequest 의 header 에서 HTTP_RANGE 라는 정보를 받아 range_match 값이 있다면
        first_byte, last_byte = range_match.groups()
        # 정규표현식으로 추출해낸 range_match 의 첫번째 요소를 first_byte, 두번째 요소를 last_byte 로 할당
        first_byte = int(first_byte) if first_byte else 0
        # 초기 바이트값이 있다면 정수화 / 없다면 0 으로 지정
        last_byte = int(last_byte) if last_byte else size - 1
        # 종결 바이트값이 있다면 정수화 / 없다면 size 에서 -1
        if last_byte >= size:
        # 종결 바이트값이 size 보다 크거나 같다면
            last_byte = size - 1
            # size 에서 -1
        length = last_byte - first_byte + 1
        # length 는 종결 바이트값에서 초기 바이트값을 뺀 뒤 +1 을 한 값

        resp = StreamingHttpResponse(RangeFileWrapper(open(path, 'rb'), offset=first_byte, length=length), status=206, content_type=content_type)
        resp['Content-Length'] = str(length)
        resp['Content-Range'] = 'bytes %s-%s/%s' % (first_byte, last_byte, size)
    else:
        resp = StreamingHttpResponse(FileWrapper(open(path, 'rb')), content_type=content_type)
        resp['Content-Length'] = str(size)
    resp['Accept-Ranges'] = 'bytes'
    return resp
