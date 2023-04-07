# 아이디어 : 1. 다익스트라 | graph, distance(INF), heapq
#          2. 양방향 도로
#          3. start -> g -> h -> end
#             start -> h -> g -> end
#             == 
#             start -> end
# 알고리즘 : 다익스트라
# 자료구조 : heap (heapq)

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

# 다익스트라 함수 정의 -> distance 리스트 return
def dijkstra(start) :
    # 거리테이블 초기화
    distance = [INF] * (n + 1)
    
    # 힙큐 및 시작노드 초기화
    hq = []
    heapq.heappush(hq, (0, start)) # (거리, 노드) 순으로 저장
    distance[start] = 0
    
    # 힙큐가 빌 때까지
    while hq :
        dist, now = heapq.heappop(hq)
        
        # 기존거리가 더 짧다면 무시
        if distance[now] < dist :
            continue
        
        for v, d in graph[now] :
            cost = dist + d
            
            # 갱신거리가 더 짧다면
            if distance[v] > cost :
                distance[v] = cost
                heapq.heappush(hq, (cost, v))

    return distance

T = int(input())

for _ in range(T) :
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m) :
        a, b, d = map(int, input().split())
        # 양방향
        graph[a].append((b, d))
        graph[b].append((a, d))

    targets = []
    for _ in range(t) :
        x = int(input())
        targets.append(x)

    # 후보지 오름차순 
    targets.sort()

    s_dist = dijkstra(s)

    g_dist = dijkstra(g)
    h_dist = dijkstra(h)

    for e in targets :
        if (s_dist[e] == s_dist[g] + g_dist[h] + h_dist[e]) or (s_dist[e] == s_dist[h] + h_dist[g] + g_dist[e]) :
            print(e, end=' ')
                
    print()