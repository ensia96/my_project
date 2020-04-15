#                                                    @                      @
#   @@@@@@@@@@@        @@@@@@@@@@@     @@@@@@@@@     @         @@@@@@@@@    @
#             @        @                       @     @         @            @
#   @@@@@@@@@@@        @               @@@@@@@@@     @         @@@@@@@@@    @
#            @         @@@@@@@@@@@             @     @@@@@@    @            @@@@@@
#        @                                    @      @         @@@@@@@@@    @
#        @                                           @                      @
# @@@@@@@@@@@@@@@@   @@@@@@@@@@@@@@@@                @                      @


# def get_len_of_str(string):
#     alist = []
#     for i in string:
#         if string.count(i) > 1:
#     	    a = string.split(i)
#     for j in a:
#         b = len(j)
#         alist.append(b)
#     alist.sort()
#     return alist[-1]
# 
# 
# get_len_of_str("sdfwevdfggtehbd")

def roman_to_num(string):
    calculate = []
    calculate.append(string.count('M') * 1000)
    calculate.append(string.count('D') * 500)
    calculate.append(string.count('C') * 100)
    calculate.append(string.count('L') * 50)
    calculate.append(string.count('X') * 10)
    calculate.append(string.count('V') * 5)
    calculate.append(string.count('I') * 1)
    if 'CM' in string:
        calculate.append(-100)
    if 'CD' in string:
        calculate.append(-100)
    if 'XC' in string:
        calculate.append(-10)
    if 'XL' in string:
        calculate.append(-10)
    if 'IX' in string:
        calculate.append(-1)
    if 'IV' in string:
        calculate.append(-1)
        
    print(calculate)
    result = 0
    for i in calculate:
        result = result + i
    print(result)

roman_to_num('MCMXCIV')