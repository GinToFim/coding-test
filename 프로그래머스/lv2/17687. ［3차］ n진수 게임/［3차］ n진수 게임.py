def solution(n, t, m, p):
    num = t * m
    string = ''
    result = ''
    string = ''
    
    for i in range(num):
        string += num_to_base(i, n) # i(번째)를 n진법으로 변환
        
    for i in range(p-1, num, m):
        # print(p-1, i, string[i])
        result += string[i]
    
    return result

def num_to_base(n, base) :
    T = '0123456789ABCDEF'
    q, r = divmod(n, base)
    
    return num_to_base(q, base) + T[r] if q > 0 else T[r]