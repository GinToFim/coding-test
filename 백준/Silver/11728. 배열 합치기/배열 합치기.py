# 아이디어
# 알고리즘 : 투 포인터

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = [0 for _ in range(n + m)]
i, j, k = 0, 0, 0

while k < (n + m):
    # B의 원소를 다 채웠거나 A의 원소가 있으면서 더 적은 경우
    if j >= m or (i < n and A[i] < B[j]) :
        result[k] = A[i]
        i += 1
    # A의 원소를 다 채웠거나 B의 원소가 있으면서 더 적은 경우
    else :
        result[k] = B[j]
        j += 1
        
    k += 1
        
print(*result)