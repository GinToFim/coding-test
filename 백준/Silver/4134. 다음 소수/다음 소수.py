import math
import sys
input = sys.stdin.readline

def is_prime_number(x) :
    # x가 1이면 소수 X
    if x == 1 or x == 0 : return False
    
    for i in range(2, int(math.sqrt(x)) + 1) :
        if x % i == 0 :
            return False # 소수 X
    
    return True # 소수

T = int(input())

for _ in range(T) :
    n = int(input())
    
    while True :
        if is_prime_number(n) :
            print(n)
            break
        else :
            n += 1