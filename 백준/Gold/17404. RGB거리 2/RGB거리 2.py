import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
rgb = [list(map(int, input().split()))
        for _ in range(n)]

R, G, B = 0, 1, 2
result = INF

for color in range(3):
    # dp 테이블 초기화
    dp = [[INF] * 3 for _ in range(n)]

    # 첫 번째 행의 컬러만 초기화
    dp[0][color] = rgb[0][color]

    for i in range(1, n):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + rgb[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + rgb[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + rgb[i][B]

    # 마지막 행과 다른 색일 때만
    for j in range(3):
        if j != color:
            result = min(result, dp[n-1][j])

print(result)