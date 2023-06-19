# 아이디어
# 알고리즘 : prime number

import math

n = int(input())

# 에라토스테네스의 체
is_prime = [True for _ in range(n + 1)]
# 0과 1은 소수 X
is_prime[0] = False
is_prime[1] = False

for num in range(2, int(math.sqrt(n)) + 1) :
    if is_prime[num] == True :
        j = num * 2
        while j <= n :
            is_prime[j] = False
            j += num

# 소수를 담을 리스트
prime_nums = []

for num in range(2, n + 1) :
    if is_prime[num] :
        prime_nums.append(num)

result = 0
interval_sum = 0
start, end = 0, 0

for start in range(len(prime_nums)) :
    # 부분합이 적으면서 end가 소수 개수보다 적을 때
    while interval_sum < n and end < len(prime_nums) :
        interval_sum += prime_nums[end]
        end += 1
        
    if interval_sum == n :
        result += 1
    
    interval_sum -= prime_nums[start]
    
print(result)