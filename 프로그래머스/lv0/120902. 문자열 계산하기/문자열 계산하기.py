def solution(my_string):
    # 공백을 기준으로 나누기
    my_list = my_string.split()

    result = int(my_list[0])
    flag = 1
    
    for i in range(1, len(my_list)) :
        if my_list[i] == '+' :
            flag = 1
        elif my_list[i] == '-' :
            flag = -1
        else :
            result += flag * int(my_list[i])

    
    return result