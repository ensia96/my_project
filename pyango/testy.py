def get_len_of_str(string):
    alist = []
    for i in string:
        if string.count(i) > 1:
    	    a = string.split(i)
    for j in a:
        b = len(j)
        alist.append(b)
    alist.sort()
    return alist[-1]


get_len_of_str("sdfwevdfggtehbd")