import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bag = [list(map(int, input().split()))
       for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = bag[i-1][0]
        value = bag[i-1][1]

        # 담을 수 있는 무게가 더 작다면
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else: # 현재 보석을 담을 수 있다면
            dp[i][j] = max(value + dp[i-1][j - weight], dp[i-1][j])

print(dp[n][k])