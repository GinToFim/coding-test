# 아이디어
# 알고리즘 : 

from collections import Counter

def solution(k, tangerine):
    answer = 0
    length = len(tangerine)
    
    tan_cnt = Counter(tangerine)
    tan_cnt = list(tan_cnt.items())
    
    # 개수를 중심으로 내림차순 정렬
    tan_cnt.sort(key = lambda x : x[1], reverse=True)
    
    while tan_cnt :
        tanger, cnt = tan_cnt.pop()
        
        if length - cnt < k :
            tan_cnt.append((tanger, cnt))
            break
        
        if length - cnt == k :
            break
        
        length -= cnt
        
        
    
    return len(tan_cnt)