# 아이디어 : 
# 알고리즘 : prefix sum, two pointer

def solution(sequence, k):
    answer = []
    n = len(sequence)
    start, end = 0, 0
    now_length = 1e9
    hap = 0
    
    for start in range(n):
        while end < n and hap < k :
            hap += sequence[end]
            end += 1
        
        if hap == k :
            if end - start < now_length :
                now_length = end - start
                answer = [start, end - 1]
        
        hap -= sequence[start]
                

    return answer