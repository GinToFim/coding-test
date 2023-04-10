from itertools import combinations

def solution(numbers):
    answer = - 10 ** 9
    
    for num1, num2 in combinations(numbers, 2) :
        answer = max(answer, num1 * num2)
    
    return answer