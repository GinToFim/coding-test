# 아이디어: 1. graph, distance, heapq 정의
#           2. 특정 정점에서 모든 정점 사이의 거리 확인
# 알고리즘: 다익스트라
# 자료구조: 힙(heapq)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

# 인접 그래프 정의
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 알고리즘 정의
def dijkstra(start):
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

            # 갱신하는 길이가 더 짧다면
            if distance[v] > cost:
                distance[v] = cost
                heapq.heappush(hq, (cost, v))

    return distance


distance = dijkstra(start)
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)