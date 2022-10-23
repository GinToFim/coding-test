def solution(emergency):
    result = [0] * len(emergency)
    
    rank = 1
    while sum(emergency) > 0 :
        idx = emergency.index(max(emergency))
        emergency[idx] = 0
        result[idx] = rank
        rank += 1
    
    return result