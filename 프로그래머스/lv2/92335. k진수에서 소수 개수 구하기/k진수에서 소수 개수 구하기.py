# 아이디어 : k진수로 바꾼뒤에 0으로 split하기
#          1. k진수로 바꾸는 함수 만들기
#          2. k진수로 나온 숫자를 0으로 split 
#          3. 소수 구하는 함수 만들기
# 알고리즘 
# 자료구조 : 생략

import math

def solution(n, k):
    answer = 0
    
    n = convert_notation(n, k)
    num_list = n.split('0')
    
    for str_num in num_list :
        if str_num == '' :
            continue
        
        if is_prime(int(str_num)) :
            answer += 1
    
    return answer

def convert_notation(n, base) :
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    
    return convert_notation(q, base) + T[r] if q > 0 else T[r]

def is_prime(num) :
    if num == 0 or num == 1 : 
        return False
    
    for x in range(2, int(math.sqrt(num))+1) :
        if num % x == 0 :
            return False
    
    return True
