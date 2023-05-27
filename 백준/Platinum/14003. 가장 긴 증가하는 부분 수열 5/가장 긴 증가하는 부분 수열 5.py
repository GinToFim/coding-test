# 알고리즘 : LIS - Binary Search

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [data[0]]
tracking = [(0, data[0])]
LIS_length = 1

for x in data[1:]:
    if x > dp[-1]:
        dp.append(x)
        tracking.append((LIS_length, x))
        LIS_length += 1
    else:
        idx = bisect.bisect_left(dp, x)
        dp[idx] = x
        tracking.append((idx, x))

print(LIS_length)

result = []
LIS_length -= 1

for idx, x in tracking[::-1]:
    if idx == LIS_length:
        result.append(x)
        LIS_length -= 1

print(*result[::-1])