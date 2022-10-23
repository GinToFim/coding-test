import math

def solution(n):
    answer = 0
    
    for i in range(1, int(math.sqrt(n)) + 1) :
        if n % i == 0 :
            answer += 2
        
    if int(math.sqrt(n)) == math.sqrt(n) :
        answer -= 1
    
    return answer