# 아이디어 : 이 정도 사이의 거리라면 공유기 설치가 가능한가?
# 알고리즘 : 이분 탐색, 파라메트릭 서치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]

# 공유기 오름차순 정리
data.sort()

start = 1
end = data[-1] - data[0]
result = 0

while start <= end :
    mid = (start + end) // 2
    total = 1 # 공유기 설치 개수 (첫 번째 포함)
    now = data[0]
    
    for x in data[1:] :
        # 만약 인접한 두 공유기 사이의 거리가 충분하다면
        if mid + now <= x :
            total += 1
            now = x
            
    # 공유기 설치 대수가 충분하다면
    # 상한선 내리기
    if total >= c :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)