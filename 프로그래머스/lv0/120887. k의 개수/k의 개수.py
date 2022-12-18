def solution(i, j, k):
    answer = 0
    k = str(k)
    
    for num in range(i, j + 1) :
        string = str(num)
        for ch in string :
            if ch == k :
                answer += 1
        
    return answer