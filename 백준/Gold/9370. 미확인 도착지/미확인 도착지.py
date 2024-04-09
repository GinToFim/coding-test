# 아이디어: 0. graph, distance, heapq, 양방향
#           1. distance 테이블 3개의 만들기 (s, g, h)
#           2. 시작점 -> 목적지 와 (g, h) 경유했을 때 거리가 똑같다면 후보지
# 알고리즘: 다익스트라
# 자료구조: heaqp

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    # 거리 테이블 정의
    distance = [INF for _ in range(n + 1)]

    # 힙큐 및 시작점 정의
    hq = []
    heapq.heappush(hq, (0, start)) # (거리, 노드) 순으로 저장
    distance[start] = 0 

    # 힙큐가 빌 때까지
    while hq:
        dist, now = heapq.heappop(hq)

        # 이미 처리된 적이 있다면
        if distance[now] < dist:
            continue
            
        for v, d in graph[now]:
            cost = dist + d

            # 갱신되는 거리가 더 짧다면
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(hq, (cost, v))

    return distance

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    candidates = [int(input()) for _ in range(t)]
    candidates.sort() # 오름차순 정렬

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    destination = []

    for c in candidates:
        if ((dist_s[c] == dist_s[g] + dist_g[h] + dist_h[c]) 
            or (dist_s[c] == dist_s[h] + dist_h[g] + dist_g[c])):
            destination.append(c)

    print(*destination)