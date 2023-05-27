# 아이디어 : right - left = k + 1
# 알고리즘 : prefix sum

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

sum_value = 0
dp = [0]

for x in data :
    sum_value += x
    dp.append(sum_value)
    
result = -1e9

for i in range(n - k + 1):
    num = dp[i + k] - dp[i]
    result = max(result, num)

print(result)