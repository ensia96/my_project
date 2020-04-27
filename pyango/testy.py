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

    # for m in alist:
    #     for n in blist:
    #         if 'i' in m
    #result = 0
    # for m in alist: # m 은 a 인자를 실수부분과 허수부분으로 나눈 상태
    #     for n in blist: # n 은 b 인자를 실수부분과 허수부분으로 나눈 상태
    # result += 
    # return result


# complexNumberMultiply('11133i', '5+6i')

    # a = x + yi 로 들어올 예정
    # b = z + mi 로 들어올 예정
    
    # i = -1 의 제곱근 -> i 의 제곱 = -1
    # (a+b) * (x+y) = ax+ay+bx+by
    # str slice => list

def factorial(n):
    if (n == 0):
        return 1
    
    return n * factorial(n-1)
  

def factorial(n):
	result = 1
	for i in range(n):
		result *= (i+1)
	return result




#class DetailView(View):
#    def get(self,request,product_code):
#        product = Product.objects.get(code = product_code)
#        series = Series.objects.filter(product = product.id)
#        medias = Media.objects.filter(product = product.id)
#        list_code  = []
#        list_image = []
#        list_media = []
#
#        for content in series:
#            list_code.append(content.code)
#            list_image.append(content.image)
#        for media in medias:
#            list_media.append(media.media_url)
#
#        data = [{
#            'code'         : product.code,
#            'name'         : product.name,
#            'price'        : product.price,
#            'gender'       : product.gender,
#            'summary'      : product.detail.summary,
#            'size_img'     : product.detail.size_img,
#            'series_code'  : list_code,
#            'series_image' : list_image,
#            'media_url'    : list_media,
#            'description'  : product.detail.description,
#            'desc_img'     : product.detail.desc_img,
#            'information'  : product.detail.information,
#        }]
#        return JsonResponse({'product_detail': data},status=200)

#class CategoryView(View):
#    def get(self,request):
#        data_list = []
#        products = Product.objects.all()
#
#        for i in range(1,10):
#            product = Product.objects.get(id=i)
#            media_list = list(Media.objects.filter(product=i))[0]
#            hover_list = list(Media.objects.filter(product=i))[1]
#            data_list.append({
#                'code'        : product.code,
#                'name'        : product.name,
#                'price'       : product.price,
#                'image'       : media_list.media_url,
#                'hover_image' : hover_list.media_url,
#
#            })
#        return JsonResponse({'shoes':data_list},status=200)
