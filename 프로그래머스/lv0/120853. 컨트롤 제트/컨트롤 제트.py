def solution(s):
    answer = 0
    
    for ch in s.split() :
        if ch == 'Z' :
            answer -= value
        else :
            value = int(ch)
            answer += value
    
    return answer