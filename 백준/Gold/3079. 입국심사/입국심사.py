# 아이디어: 이 정도 시간이면 충분히 처리 가능한가? O, X
# 알고리즘: 이진 탐색, 파라메트릭

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

start, end = 0, max(data) * m

while start <= end:
    mid = (start + end) // 2
    total = sum(mid // x for x in data)
    # 이 정도 시간이면 충분하다면
    if total >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(result)