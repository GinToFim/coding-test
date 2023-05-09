# 아이디어 : 매번 queue에서 최솟값을 뽑음 -> heapq
# 알고리즘 : 선행 관계 -> 위상정렬(graph, indegree)
# 자료구조 : queue(deque), heapq

import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 그래프 및 진입차수 초기화
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
result = []  # 위상 정렬 결과

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    # a -> b
    graph[a].append(b)
    indegree[b] += 1

# 큐 정의 및 진입차수 0
hq = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(hq, i)

# 큐가 빌 때까지
while hq:
    now = heapq.heappop(hq)
    result.append(now)

    # 해당 노드와 인접한 노드 진입차수 1씩 빼기
    for v in graph[now]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(hq, v)

print(*result)