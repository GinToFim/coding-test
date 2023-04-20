# 아이디어
# 알고리즘
# 자료구조

def solution(a, b, n):
    answer = 0
    remain = 0
    
    while n >= a :
        answer += (n // a) * b
        tmp = n
        n -= (tmp // a) * a
        n += (tmp // a) * b

    
    return answer