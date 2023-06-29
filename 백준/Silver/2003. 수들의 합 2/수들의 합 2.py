# 아이디어 : 
# 알고리즘 : prefix sum, two pointer

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

# 누적합 초기화
dp = [0] 
sum_value = 0

for x in data :
    sum_value += x
    dp.append(sum_value)
    
start, end = 0, 0
result = 0

for start in range(n+1):
    while end < n and (dp[end] - dp[start]) < m :
        end += 1
    
    if (dp[end] - dp[start]) == m :
        result += 1
    
print(result)