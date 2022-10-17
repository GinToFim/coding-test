# 아이디어 : 1. 10진법 to n진법 함수 정의
#           2. 모든 사람들이 말하는 개수 만큼 숫자 나열
#           3. 튜브가 말하는 순서에 해당하는 문자 담기
# 알고리즘 : 구현

def solution(n, t, m, p):
    num = t * m # 총 숫자의 개수
    string = '' # 숫자를 나열할 문자열
    result = '' # 튜브가 말해야하는 숫자(문자열)
    
    for i in range(num) :
        string += convert_notation(i, n)
    
    for i in range(num) :
        if (i+1) % m == p % m :
            result += string[i]
    
    return result

# n진법 변환 함수
def convert_notation(n, base) :
    T = '0123456789ABCDEF'    
    q, r = divmod(n, base)
    
    return convert_notation(q, base) + T[r] if q > 0 else T[r]