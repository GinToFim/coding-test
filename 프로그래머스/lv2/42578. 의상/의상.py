# 아이디어 : (종류1 개수 + 1) * (종류2 개수 + 1) - 1(아무것도 입지 않음)
# 알고리즘 : hash
# 자료구조 : dict

from collections import defaultdict

def solution(clothes):
    closet = defaultdict(list)
    
    for clothe, _type in clothes :
        closet[_type].append(clothe)
        
    result = 1
    for _type in closet :
        result *= len(closet[_type]) + 1
    
    # 아무것도 입지 않은 case 빼기
    return result - 1