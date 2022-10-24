def solution(numbers, k):
    answer = 0
    idx = -2
    while k > 0 :
        idx += 2
        if idx >= len(numbers) :
            idx -= len(numbers)
        k -= 1
        
    return idx + 1