import heapq
import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split()))
        for _ in range(n)]

# 오름차순 정렬
data.sort()

# 힙큐 초기화
hq = [data[0][1]]

for start, end in data[1:]:
    # 다음 강의가 시작이 가능하다면 
    if start >= hq[0]:
        heapq.heappop(hq)
    
    heapq.heappush(hq, end)

print(len(hq))