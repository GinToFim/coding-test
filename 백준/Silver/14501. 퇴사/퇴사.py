# 아이디어 : 
# 알고리즘 : dp

import sys
input = sys.stdin.readline

n = int(input())
times = []
prices = []

for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)
    
dp = [0 for _ in range(n + 1)]

for i in range(n-1, -1, -1):
    # 상담진행이 가능하다면
    if i + times[i] <= n :
        dp[i] = max(prices[i] + dp[i + times[i]], dp[i+1])
    # 상담진행이 불가능하다면
    else :
        dp[i] = dp[i+1]
        
print(dp[0])