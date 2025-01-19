import sys
input = sys.stdin.readline

n = int(input())

data = [list(map(int, input().split()))
        for _ in range(n)]

# dp 테이블 선언
dp = [[0] * 3 for _ in range(n)]

# 첫 번째는 그대로 복사
dp[0] = data[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]

print(min(dp[n-1]))