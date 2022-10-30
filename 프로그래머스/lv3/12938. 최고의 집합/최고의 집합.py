# 아이디어
# 알고리즘
# 자료구조

def solution(n, s):
    # 만약 s(원소들의 합)가 n(자연수의 개수)보다 작다면
    if n > s :
        return [-1]
    
    result = [s//n] * n
    
    idx = len(result) - 1
    sum_value = sum(result)
    
    while sum_value < s :
        sum_value += 1
        result[idx] += 1
        idx += -1
    
    return result