# 아이디어 : 1. 약수의 개수 구하기(제곱근) 
#           2. 도중에 개수가 limit를 넘어가면 power만큼 추가하기
# 알고리즘 : number theory - divisor

import math

def solution(number, limit, power):
    divisor = [1] # 1의 약수는 무조건 1개
    
    for num in range(2, number + 1) :
        cnt = 0 # 약수의 개수
        for i in range(1, int(math.sqrt(num)) + 1) :
            # num가 i로 나누어 떨어진다면
            if num % i == 0 :
                # num가 제곱수라면
                if num == i ** 2 :
                    cnt += 1
                else :
                    cnt += 2
        
        if cnt > limit :
            divisor.append(power)
        else :
            divisor.append(cnt)
    
    return sum(divisor)