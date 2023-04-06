# 아이디어 : 가능한 몇분으로 해야 블루레이의 크기를 최소화하는가?
#           -> 이 시간 정도면 블루레이 크기가 가능한가? Yes or No?
# 알고리즘 : 이진 탐색, 파라메트릭 서치

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 10**10
result = sum(data)

while start <= end :
    mid = (start + end) // 2
    if mid < max(data):
        start = mid + 1
        continue
    
    cnt = 1 # 녹화 개수 
    total = 0 # 블루레이 크기
    
    for i in range(len(data)) :
        if data[i] + total > mid :
            total = data[i] # 녹화시간 초기화
            cnt += 1
        else :
            total += data[i]
    
    
    if cnt <= m :
        result = min(result, mid)
        end = mid - 1
    else :
        start = mid + 1
    
print(result)
        