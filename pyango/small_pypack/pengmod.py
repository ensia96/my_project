class MySet:
  def __init__(self, size):
    self.size = size
    self.bucket = [ None for x in range(size) ] # => [ None 의 개수가 size 만큼 있다. ]

  def values(self):
    set_data =""
    for i in range(self.size):
      if self.bucket[i] != None:
        set_data += self.bucket[i]
        set_data += ", "
    if set_data[-1] == " ":
      data_set = set_data[:-2]
    return data_set

  # 1. hash_value 함수
  def hash_value(self,key):
    hash_value = hashlib.sha1(key.encode())
    # 여기서 부터 구현
  
  # 2. add 함수
  def add(self, key):
    hash_value = self.hash_value(key)
    # 여기서 부터 구현

print(MySet)