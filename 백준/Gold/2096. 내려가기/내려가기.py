# 아이디어
# 알고리즘 : dp

import sys
input = sys.stdin.readline

n = int(input())
max_prev = list(map(int, input().split()))
min_prev = [x for x in max_prev]

max_now = [0 for _  in range(3)]
min_now = [0 for _  in range(3)]

for _ in range(n-1) :
    a, b, c = map(int, input().split())
    
    max_now[0] = a + max(max_prev[0], max_prev[1])
    max_now[1] = b + max(max_prev)
    max_now[2] = c + max(max_prev[1], max_prev[2])
    
    min_now[0] = a + min(min_prev[0], min_prev[1])
    min_now[1] = b + min(min_prev)
    min_now[2] = c + min(min_prev[1], min_prev[2])
    
    max_prev = [x for x in max_now]
    min_prev = [x for x in min_now]
    
print(max(max_prev), min(min_prev))