import math

def solution(denum1, num1, denum2, num2):
    denomi = LCM(num1, num2)
    numer = denum1 * (denomi // num1)
    numer += denum2 * (denomi // num2)
    
    # 기약분수가 아니라면
    gcd_num = math.gcd(numer, denomi)
    if gcd_num > 1 :
        numer //= gcd_num
        denomi //= gcd_num
    
    return [numer, denomi]

def LCM(num1, num2) :
    return num1 * num2 // math.gcd(num1, num2)