# 아이디어 : 1 // 2, 2 // 2 = 0, 1
#           -> (1+1) // 2, (2+1)//2 = 1, 1
# 알고리즘 : O(logN) = log2^20 = 20
# 자료구조 : X

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer