def fac(x) :
    if x == 0 :
        return 1
    
    return x * fac(x-1)

def solution(n):
    x = 0
    while n >= fac(x):
        x += 1
    
    return x - 1