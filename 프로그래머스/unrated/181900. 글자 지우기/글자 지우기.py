def solution(my_string, indices):
    answer = ''
    indices.sort(reverse=True)
    num = indices.pop()
    
    for i in range(len(my_string)) :
        if num == i :
            if len(indices) > 0 :
                num = indices.pop()
            continue
        
        answer += my_string[i]
    
    return answer