import sys
input = sys.stdin.readline

n, w = map(int, input().split())
bag = [(0, 0)]

for i in range(n):
    bag.append(tuple(map(int, input().split())))

dp = [[0] * (w + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, w + 1):
        weight = bag[i][0]
        value = bag[i][1]

        if j < weight: # 담을 수 없다면
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])

print(dp[n][w])