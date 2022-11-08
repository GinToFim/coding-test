# 아이디어 : 1. scope를 정렬하고, times_dict 만들기
# 알고리즘
# 자료구조

def solution(distance, scope, times):
    n = len(scope)
    for i in range(n) :
        scope[i].sort()
        scope[i].append(i)
    scope.sort()
    
    times_dict = {i : times[i] for i in range(n)}
    
    for i in range(n) :
        start, end, key = scope[i]
        work, rest = times_dict[key]
        
        for num in range(start, end + 1) :
            if (num-1) % (work + rest) <= work-1 :
                return num
        
    return distance