# 아이디어 : start 노드에서 가는데 가능한 개수와 최대 가중치 출력
# 알고리즘 : 다익스트라(graph, distance, heapq)
# 자료구조 : heapq(heap)

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

        # 이미 처리된 적이 있다면 무시
        if distance[now] < dist :
            continue
        
        for v, d in graph[now] :
            cost = dist + d
            
            # 갱신 거리가 기존 거리보다 짧다면
            if cost < distance[v] :
                distance[v] = cost
                heapq.heappush(hq, (cost, v))

T = int(input())

for _ in range(T) :
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(d) :
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    distance = [INF] * (n + 1)    

    # 다익스트라 알고리즘 수행
    dijkstra(c)

    cnt = 0 # 바이러스 걸린 대수
    result = 0 # 바이러스 걸리는 시간

    for d in distance :
        if d < INF :
            cnt += 1
            result = max(result, d)

    print(cnt, result)