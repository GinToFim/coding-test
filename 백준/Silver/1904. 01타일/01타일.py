# 아이디어: 피보나치
# 알고리즘: DP

import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1) :
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
print(dp[n])