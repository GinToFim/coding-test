def solution(age):
    age_dict = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e',
                5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
    
    result = ''
    while age > 0 :
        result += age_dict[age%10]
        age //= 10
        
    return result[::-1]