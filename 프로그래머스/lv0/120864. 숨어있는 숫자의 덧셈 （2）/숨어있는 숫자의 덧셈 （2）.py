def solution(my_string):
    answer = 0
    
    num = 0
    for ch in my_string :
        if ch.isalpha() :
            answer += num
            num = 0
        else :
            num = num * 10 + int(ch)
    
    # 안나온 숫자가 있다면 추가
    answer += num
    
    return answer