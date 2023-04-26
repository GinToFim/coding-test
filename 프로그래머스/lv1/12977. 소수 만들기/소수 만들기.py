# 아이디어 : 1. 주어진 숫자 중 3개의 조합 (combinations)
#           2. 그 수가 소수인지 판단 (is_prime)
# 알고리즘 : combination & is_prime

import math
from itertools import combinations

def is_prime(x) :
    # 1이면 소수 X
    if x == 1 :
        return False
    
    for i in range(2, int(math.sqrt(x)) + 1) :
        # x가 i로 나누어 떨어진다면
        if x % i == 0 :
            return False
    
    # 모든 수가 나누어 떨어지지 않는다면
    return True

def solution(nums):
    answer = 0

    for iters in combinations(nums, 3) :
        if is_prime(sum(iters)) :
            answer += 1

    return answer