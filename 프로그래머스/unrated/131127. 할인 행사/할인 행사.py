# 아이디어
# 알고리즘 
# 자료구조 : 해시-맵 사용, dict 사용

def solution(want, number, discount):
    discount_dict = dict()
    
    for i in range(len(discount)-10+1) :
        sort_discount = sorted(discount[i:i+10])
        key = ''.join(sort_discount)
        
        if key not in discount_dict :
            discount_dict[key] = 1
        else :
            discount_dict[key] += 1
    
    want_list = []
    for i in range(len(want)) :
        for _ in range(number[i]) :
            want_list.append(want[i])

    want_key = ''.join(sorted(want_list))
    
    if want_key in discount_dict.keys() :
        return discount_dict[want_key]
    else :
        return 0