import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# dp 테이블 갱신
dp = [1 for x in range(n)]

for i in range(n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))