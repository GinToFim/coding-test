def solution(hp):
    answer = 0
    ants = [5, 3, 1]
    
    for ant in ants :
        answer += hp // ant
        hp %= ant
    
    return answer