# 아이디어 : 1. graph, distance, heap 정의
#            2. 양방향성
#            3. (1 -> u -> v -> n) or (1 -> v -> u -> n) 둘 중에 하나가 최소
# 알고리즘 : dijkstra
# 자료구조 : heapq

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

# 그래프 정의
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    


u, v = map(int, input().split())

def dijkstra(start):
    # 거리 테이블 정의
    distance = [INF for _ in range(n + 1)]
    
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (0, start)) # (거리, 노드)순으로 저장
    distance[start] = 0
    
    # 힙큐가 빌 때까지
    while hq:
        dist, now = heapq.heappop(hq)
        
        # 이미 처리된 적이 있다면
        if distance[now] < dist:
            continue
            
        for v, d in graph[now]:
            cost = dist + d
            # 기존 거리보다 갱신 거리가 크다면
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(hq, (cost, v))
                
    return distance

dist_1 = dijkstra(1)
dist_u = dijkstra(u)
dist_v = dijkstra(v)
                
path1 = dist_1[u] + dist_u[v] + dist_v[n]
path2 = dist_1[v] + dist_v[u] + dist_u[n]

result = min(path1, path2)

if result >= INF:
    print(-1)
else :
    print(result)