# 아이디어
# 알고리즘 : prefix sum

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

sum_value = 0
dp = [0]

for x in data :
    sum_value += x
    dp.append(sum_value)
    
for _ in range(m):
    left, right = map(int, input().split())
    
    print(dp[right] - dp[left - 1])