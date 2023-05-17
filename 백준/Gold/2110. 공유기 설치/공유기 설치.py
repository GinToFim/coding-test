# 아이디어 : 1. 두 공유기 사이의 최대 거리 -> 이 정도 거리면 충분한가?
#           2. start = 1, end = max(data) - min(data)
# 알고리즘 : 이진 탐색, 파라메트릭 서치

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [int(input()) for _ in range(n)]

# 오름차순 정렬
data.sort()

start, end = 1, data[-1] - data[0]
result = 0

while start <= end :
    mid = (start + end) // 2
    
    cnt = 1 # 공유기 설치 대수 (처음 하나는 무조건 설치)
    past = data[0] # 이전 공유기 설치 위치
    
    for x in data[1:] :
        # 공유기 설치 거리가 충분하다면
        if x - past >= mid :
            cnt += 1
            past = x
    
    # 공유기 설치 대수가 충분하다면, (거리 늘리기)
    if cnt >= m :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)