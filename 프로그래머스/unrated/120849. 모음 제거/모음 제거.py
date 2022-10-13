def solution(my_string):
    answer = ''
    
    for ch in my_string :
        if ch in 'aeiou' :
            continue
        answer += ch
        
    return answer