# 아이디어 : 마지막 날에서부터 첫째 날까지 확인
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
    # 기한 내에 충분하다면
    if times[i] + i <= n :
        dp[i] = max(prices[i] + dp[i + times[i]], dp[i+1])
    else :
        dp[i] = dp[i+1]
        
print(dp[0])