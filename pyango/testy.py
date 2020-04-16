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

def more_than_half(nums):
    alist = [0]
    for i in nums:
        if alist[0] < nums.count(i):
            del alist[0]
            alist.append(nums.count(i))
    if nums.count(i) == alist[0]:
        return i

more_than_half([1,1,1,1,2,2,2,2,2,2,2,1])