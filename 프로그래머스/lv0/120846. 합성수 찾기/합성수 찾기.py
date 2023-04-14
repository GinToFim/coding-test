import math

def solution(n):
    answer = 0
    
    for x in range(2, n + 1) :
        for i in range(2, int(math.sqrt(x)) + 1) :
            if x % i == 0 :
                answer += 1
                break
    
    return answer