import hashlib

class MySet: # 내가 지정할 암호화방식 ( 몇 개의 버킷을 사용할 지 )
  def __init__(self, size): # class 의 size 인자를 받아 이니셜
    self.size = size # 인자로 받은 값으로 size 지정
    self.bucket = [ None for x in range(size) ] # 자정한 size 수 만큼 None(buacket)을 담은 list 생성

  def values(self):
    set_data ="" # 정보를 담을 set_data (기준 문자열) 생성
    for i in range(self.size): # size 범위에 대해 반복구문
      if self.bucket[i] != None: # list 의 원소들에 대해 None 이 아닌 경우의 조건구문
        set_data += self.bucket[i] # 기준 문자열에 list 의 원소 추가
        set_data += ", " # 다음에 올 원소와의 구분자 추가
    if set_data[-1] == " ": # 반복이 끝난 후의 조건구문
      data_set = set_data[:-2] # 생성된 기준 문자열을 data_set 에 할당
    return data_set # 마지막 ', ' 부분이 사라진 문자열 반환

# 1. hash_value 함수 : 이 함수는 
  def hash_value(self,key): # sha1 방식으로 구한 해시값을 16진수화 하여, 숫자형 데이터만 추출한 뒤, 버킷수로 나눈 나머지값을 출력
    hash_value = hashlib.sha1(key.encode())# 인자로 받은 key 를 인코드하고 sha1 함수로 작업
    # 여기서 부터 구현
    base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 비교대상 list 지정 ( 16진수는 숫자모양도 문자형 )
    ineed="" # 정보를 담을 ineed (기준 문자열) 생성
    for t in hash_value.hexdigest(): # sha1 방식으로 암호화된 값을 16진수화한 상태의 요소들에 대한 반복구문
      if t in base: # 비교대상 list 와의 비교를 통한 조건 구문
        ineed += t # 조건 만족값들을 기준 문자열에 추가
    return int(ineed) % self.size # 추출된 기준 문자열을 정수화한 뒤 class 의 size 값으로 나눈 나머지를 return

# 2. add 함수
  def add(self, key):
    hash_value = self.hash_value(key) # 같은 class 의 함수내용 호출
    # 여기서 부터 구현
    if key in self.bucket: # 버킷 안에 같은 값이 있다면
      return self.bucket # 아무것도 하지마!
    for i in range(self.size): # 사이즈에 대해서 반복구문
      if (hash_value+i)<self.size: # size 를 넘어가지 않는다면
        if self.bucket[hash_value+i]==None: # 그 위치의 값이 비어있다면
          self.bucket[hash_value+i]=key # 그 위치에 키를 넣어
          return self.bucket # 그리고 결과를 내줘
      else: # size 를 넘어간다면
        if self.bucket[hash_value+i-self.size]==None: # 그 위의 값이 비어있다면
          self.bucket[hash_value+i-self.size]=key # 그 위치에 키를 넣어
          return self.bucket # 그리고 결과를 내줘