# 아이디어 : 1. 가장 긴 감소하는 수열
# 알고리즘 : LIS - dp (n = 2000 -> n^2=4*10^6)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(n - max(dp))