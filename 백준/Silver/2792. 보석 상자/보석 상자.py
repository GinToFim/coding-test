# 아이디어 : 1. 질투값의 최소 -> 이 정도 질투값이면 충분한가?
#           2. start = 1, end = max(data)
# 알고리즘 : 이진탐색, 파라메트릭 서치

import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(m)]

start, end = 1, max(data)
result = 0

while start <= end :
    mid = (start + end) // 2
    
    total = 0 # 보석을 나누어 가진 학생 수
    for x in data :
        total += math.ceil(x / mid)
    
    # 이 정도 학생수로 다 나누어 가졌으면, 상한선 내리기
    if total <= n :
        result = mid
        end = mid - 1
    else :
        start = mid + 1


print(result)