# 아이디어
# 알고리즘 : sort

def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    idx = 0
    
    for a in A :
        if a < B[idx] :
            idx += 1
    
    return idx