# 아이디어 : 
# 알고리즘 : LCS - binary search

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [data[0]]

for x in data[1:]:
    if dp[-1] < x :
        dp.append(x)
    else :
        idx = bisect.bisect_left(dp, x)
        dp[idx] = x
        
print(len(dp))