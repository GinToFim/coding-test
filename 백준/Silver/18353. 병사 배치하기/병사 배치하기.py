# 아이디어 : LDS -> LIS 변경
# 알고리즘 : LIS - Binary Search

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data.reverse() # 배열 뒤집기

dp = [data[0]]

for x in data[1:]:
    if dp[-1] < x :
        dp.append(x)
    else:
        idx = bisect.bisect_left(dp, x)
        dp[idx] = x

print(n - len(dp))