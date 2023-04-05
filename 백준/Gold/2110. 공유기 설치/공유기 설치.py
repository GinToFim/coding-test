import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = []

for _ in range(n) :
    data.append(int(input()))
    
# 이진 탐색을 위해 오름차순 정렬
data.sort()

start = 1 # 가능한 최소 거리
end = data[-1] - data[0] # 가능한 최대 거리
result = 0

while start <= end :
    mid = (start + end) // 2
    value = data[0]
    cnt = 1 # 현재 공유기 설치 대수
    
    for i in range(1, n) : # 앞에서부터 공유기 설치
        if data[i] >= value + mid : # 인접한 거리가 충분하다면
            value = data[i]
            cnt += 1
    
    # 공유기가 충분히 설치되었다면, 거리 증가
    if cnt >= c : 
        result = mid
        start = mid + 1
    # 공유기가 부족하다면, 거리 감소
    else :
        end = mid - 1

print(result)