# 아이디어 : 해당 거리가 가장 인접한 두 공유기 사이의 최대 거리인가?
#           -> 해당 거리로 공유기 설치가 충분한가?
# 알고리즘 : 이분 탐색(O(logn)), 파라메트릭 서치

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = []
for _ in range(n) :
    data.append(int(input()))
    
# 이분 탐색을 위해 오름차순 정렬
data.sort()

# end : 최대 - 최소
start, end = 1, data[-1] - data[0]

result = 0

while start <= end :
    mid = (start + end) // 2
    
    cnt = 1 # 설치 공유기 대수
    past = data[0]
    
    for i in range(1, n) :
        # 해당 위치가 전에 (공유기 위치 + 공백) 보다 충분하다면
        if data[i] >= past + mid :
            past = data[i]
            cnt += 1
    
    # 공유기가 충분히 설치되었다면
    if cnt >= c :
        result = mid
        start = mid + 1
    else :
        end = mid - 1
        
print(result)