n = int(input())

schedule = [list(map(int, input().split()))
            for _ in range(n)]

dp = [0] * (n + 1)

for i in range(n):
    term = schedule[i][0]
    price = schedule[i][1]

    
    for j in range(i + term, n + 1):
        # i번째 날짜에 일하는게 이득이라면
        if dp[j] < dp[i] + price:
            dp[j] = dp[i] + price

print(dp[n])