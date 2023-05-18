# 아이디어 
# 알고리즘 : LIS (DP - O(n^2))

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# dp 테이블 생성 - 모든 수를 1로 초기화
dp = [1 for _ in range(n)]

# 뒤에 있는 원소가 앞에 있는 원소보다 크면
# 증가하는 수열 + 1
for i in range(1, n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))