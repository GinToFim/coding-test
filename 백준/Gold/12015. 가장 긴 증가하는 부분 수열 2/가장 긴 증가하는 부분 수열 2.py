# 아이디어
# 알고리즘 : LIS - 이진 탐색

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [data[0]]

for x in data[1:]:
    if x > dp[-1]:
        dp.append(x)
    else :
        idx = bisect.bisect_left(dp, x)
        dp[idx] = x
        
print(len(dp))