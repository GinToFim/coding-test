# 아이디어 : 1. 양방향
# 알고리즘 : djikstra
# 자료구조 : heap(heapq)

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

# 다익스트라 알고리즘 정의
def dijkstra(start) :
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (0, start)) # (거리, 노드) 순으로 저장
    distance[start] = 0
    
    # 힙큐가 빌 때까지
    while hq :
        dist, now = heapq.heappop(hq)
        
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist :
            continue
        
        for v, d in graph[now] :
            cost = dist + d
            
            # 갱신거리가 현재거리보다 더 짧다면
            if cost < distance[v] :
                distance[v] = cost
                heapq.heappush(hq, (cost, v))

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m) :
    a, b, c = map(int, input().split())
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))

# 다익스트라 함수 수행
dijkstra(1)

print(distance[n])