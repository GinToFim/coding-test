# 아이디어 : 1. 가장 뒤에 오는 수가 0) 앞에는 1만 가능
#           2. 가장 뒤에 오는 수가 1~8) [j-1] + [j+1]
#           3. 가장 뒤에 오는 수가 9) 앞에는 8만 가능
# 알고리즘 : dp

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0 :
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)