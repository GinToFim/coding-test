def solution(num_list, n):
    result = [[] for _ in range(len(num_list) // n)]
    print(result)
    
    for step in range(0, len(num_list), n) :
        for i in range(n) :
            result[step//n].append(num_list[step + i])
        
    return result