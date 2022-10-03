from collections import Counter

def solution(array):
    cnt = Counter(array)
    mode_list = cnt.most_common()
    
    # 최빈값이 여러 개라면
    if len(mode_list) > 1 :
        if mode_list[0][1] == mode_list[1][1] :
            return -1
    
    return mode_list[0][0]