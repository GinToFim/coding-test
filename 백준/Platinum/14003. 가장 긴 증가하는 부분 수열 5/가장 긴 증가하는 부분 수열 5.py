# 아이디어 
# 알고리즘 : LIS - Binary Search (길이, 배열)

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [data[0]] # LIS 길이를 찾기 위한 리스트
tracking = [(0, data[0])] # LIS를 찾기 위한 리스트
LIS_length = 1

for x in data[1:]:
    if dp[-1] < x :
        dp.append(x)
        tracking.append((LIS_length, x))
        LIS_length += 1
    else :
        idx = bisect.bisect_left(dp, x)
        dp[idx] = x
        tracking.append((idx, x))

result = []
LIS_length -= 1
for i in range(n-1, -1, -1):
    if tracking[i][0] == LIS_length:
        result.append(tracking[i][1])
        LIS_length -= 1

print(len(dp))
print(*result[::-1])