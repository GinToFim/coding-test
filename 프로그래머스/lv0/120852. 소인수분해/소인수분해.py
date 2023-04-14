import math

def is_prime_number(x) :
    # 1은 소수 X
    if x == 1 : return False

    for i in range(2, int(math.sqrt(x)) + 1) :
        # x가 i로 나누어떨어진다면
        if x % i == 0 :
            return False # 소수 X
    
    return True # 소수
        
def solution(n):
    answer = []
    
    for i in range(2, n + 1) :
        # n이 i로 나누어 떨어지고 소수일 때
        if n % i == 0 and is_prime_number(i) :
            answer.append(i)
        
    
    return answer