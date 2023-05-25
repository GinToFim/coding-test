# 아이디어 : 
# 알고리즘 : 

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dist = [0]
index = [0 for _ in range(n+1)]

for i in range(n):
    x = data[i]
    
    if dist[-1] < x:
        dist.append(x)
        index[i] = len(dist) - 1
    else:
        index[i] = bisect.bisect_left(dist, x)
        dist[index[i]] = x

length = len(dist)-1
print(length)

result = []
for i in range(n, -1, -1):
    if index[i] == length:
        result.append(data[i])
        length -= 1

print(*result[::-1])