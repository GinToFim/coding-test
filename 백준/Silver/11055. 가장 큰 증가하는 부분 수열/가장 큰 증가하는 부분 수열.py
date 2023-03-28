import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = [x for x in data] # dp 테이블 초기화

for i in range(n) :
    for j in range(i) :
        if data[i] > data[j] :
            dp[i] = max(dp[i], dp[j] + data[i])

print(max(dp))