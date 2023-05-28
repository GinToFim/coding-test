# 아이디어
# 알고리즘 : 누적합

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

dp = [0]
sum_value = 0

for x in data:
    sum_value += x
    dp.append(sum_value)

result = 0

for iters in combinations(range(n+1), 2):
    left, right = iters
    if (dp[right] - dp[left]) == m:
        result += 1
        
print(result)