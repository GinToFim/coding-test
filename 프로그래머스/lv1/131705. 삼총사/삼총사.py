# 아이디어 : 13 combination 3
# 알고리즘 : itertools 의 combinations 사용
# 자료구조 

from itertools import combinations

def solution(number):
    answer = 0
    
    for num_case in combinations(number, 3) :
        if sum(num_case) == 0 :
            answer += 1
            
    return answer