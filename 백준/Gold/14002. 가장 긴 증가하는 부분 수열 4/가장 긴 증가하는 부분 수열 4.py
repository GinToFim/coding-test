# 아이디어 : 
# 알고리즘 : LIS - DP (n = 1,000 -> n^2 = 10^6)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# dp 테이블을 1로 초기화
dp = [1 for _ in range(n)]

for i in range(1, n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j] + 1)

order = max(dp)
print(order)

max_idx = dp.index(order)
lis = []

for i in range(max_idx, -1, -1) :
    if dp[i] == order :
        lis.append(data[i])
        order -= 1

print(*lis[::-1])