# 다익스트라 : heapq, graph, distacne

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF] * (n + 1)

def dijkstra(start) :
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    
    # 힙큐가 빌 때까지
    while hq :
        dist, now = heapq.heappop(hq)
        
        # 이미 처리된 적이 있다면 무시(distance[now]보다 길다면)
        if distance[now] < dist :
            continue
        
        for v, d in graph[now] :
            cost = dist + d
            # 합친 거리보다 길다면
            if cost < distance[v] :
                distance[v] = cost
                heapq.heappush(hq, (cost, v))
                
dijkstra(start)

for i in range(1, n + 1) :
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])
