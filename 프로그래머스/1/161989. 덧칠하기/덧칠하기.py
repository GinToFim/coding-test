def solution(n, m, section):
    answer = 0
    where = 0
    
    for now in section:
        if now > where:
            where = now + m - 1
            answer += 1
            
    return answer