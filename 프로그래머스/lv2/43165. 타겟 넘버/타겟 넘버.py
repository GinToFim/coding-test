# 아이디어 : 1. itertools의 product를 사용하여 중복순열 구현
#           2. 1 or -1을 중복 순열 (len(numbers)만큼)
# 알고리즘 : dfs(백트래킹) (2^20 = 1,000,000)
# 자료구조 : stack

from itertools import product

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    operators_list = [iters for iters in product((-1, 1), repeat=n)]
    
    for operators in operators_list :
        hap = 0
        for op, num in zip(operators, numbers) :
            hap += op * num
        
        if hap == target :
            answer += 1
    
    return answer