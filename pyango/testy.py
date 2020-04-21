#                                                    @                      @
#   @@@@@@@@@@@        @@@@@@@@@@@     @@@@@@@@@     @         @@@@@@@@@    @
#             @        @                       @     @         @            @
#   @@@@@@@@@@@        @               @@@@@@@@@     @         @@@@@@@@@    @
#            @         @@@@@@@@@@@            @      @@@@@@    @            @@@@@@
#        @                                   @       @         @@@@@@@@@    @
#        @                                  @        @                      @
# @@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@                @                      @


def get_len_of_str(string): # get_len_of_str("sdfwevdfggtehbd")
    alist = []
    for i in string:
        if string.count(i) > 1:
    	    a = string.split(i)
    for j in a:
        b = len(j)
        alist.append(b)
    alist.sort()
    return alist[-1]

def more_than_half(nums): # more_than_half([1,1,1,1,2,2,2,2,2,2,2,1])
    alist = [0]
    for i in nums:
        if alist[0] < nums.count(i):
            del alist[0]
            alist.append(nums.count(i))
    if nums.count(i) == alist[0]:
        return i





def complexNumberMultiply(a, b):
    alist = []
    blist = []
    if '+' in a: # 복소수일때
        aa = a.index('+')
        alist.append(a[:aa]) # 실수부분
        alist.append(a[aa+1:-1]) # 허수 앞의 숫자부분
        alist.append(a[-1]) # i
    elif 'i' in a: # 허수일때
        alist.append(a[:-1]) # 허수 앞의 숫자부분
        alist.append(a[-1]) # i
    else: # 실수일때
        alist.append(a)
    if '+' in b: # 복소수일때
        bb = b.index('+')
        blist.append(b[:bb]) # 실수부분
        blist.append(b[bb+1:-1]) # 허수 앞의 숫자부분
        blist.append(b[-1]) # i
    elif 'i' in b: # 허수일때
        blist.append(b[:-1]) # 허수 앞의 숫자부분
        blist.append(b[-1]) # i
    else: # 실수일때
        blist.append(b)

    for m in alist:
        for n in blist:
            if 'i' in m
    #result = 0
    # for m in alist: # m 은 a 인자를 실수부분과 허수부분으로 나눈 상태
    #     for n in blist: # n 은 b 인자를 실수부분과 허수부분으로 나눈 상태
    # result += 
    # return result


complexNumberMultiply('11133i', '5+6i')

# a = x + yi 로 들어올 예정
# b = z + mi 로 들어올 예정

# i = -1 의 제곱근 -> i 의 제곱 = -1
# (a+b) * (x+y) = ax+ay+bx+by
# str slice => list