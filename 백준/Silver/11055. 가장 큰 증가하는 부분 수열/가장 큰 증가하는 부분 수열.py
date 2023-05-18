# 아이디어
# 알고리즘 : LIS - DP (n = 1000 -> n^2 = 10^6 )

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 해당 원소로 dp 테이블 갱신
dp = [x for x in data]

for i in range(1, n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j] + data[i])
            
print(max(dp))