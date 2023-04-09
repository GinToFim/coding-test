# 아이디어 : 
# 알고리즘 : dijkstra(graph, heapq, distance)
# 자료구조 : heap(heapq)

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

v, e, p = map(int, input().split())
graph = [[] for _ in range(v + 1)] 

for _ in range(e) :
    a, b, c = map(int, input().split())
    # 양방향
    graph[a].append((b, c))
    graph[b].append((a, c))

# 다익스트라 알고리즘 정의
def dijkstra(start) :
    # 거리 테이블 정의
    distance = [INF] * (v + 1)
    
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (0, start)) # (거리, 노드)순으로 저장
    distance[start] = 0
    
    # 힙큐가 빌 때까지
    while hq :
        dist, now = heapq.heappop(hq)
        
        # 이미 처리된 적이 있다면 무시
        if distance[now] < dist :
            continue
            
        for i, d in graph[now] :
            cost = dist + d
            
            # 갱신 거리가 기존 거리보다 짧다면
            if cost < distance[i] :
                distance[i] = cost
                heapq.heappush(hq, (cost, i))
    
    return distance

min_dist = dijkstra(1)
gun_dist = dijkstra(p)

if min_dist[v] == (min_dist[p] + gun_dist[v]) :
    print("SAVE HIM")
else :
    print("GOOD BYE")