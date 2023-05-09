# 아이디어
# 알고리즘 : topology sort(graph, indegree)
# 자료구조 : queue(deque)

from collections import deque
import sys

input = sys.stdin.readline


def topology_sort(data, w):
    times = [-1] + data  # 해당 노드가 걸리는 시간
    result = [-1] + data  # 총 걸리는 시간
    # 큐 및 진입차수 0 정의
    queue = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)

    # 큐가 빌 때까지
    while queue:
        now = queue.popleft()

        # 해당 노드와 인접한 노드 확인
        for v in graph[now]:
            result[v] = max(result[v], result[now] + times[v])
            indegree[v] -= 1
            # 진입차수가 0이라면
            if indegree[v] == 0:
                queue.append(v)

    return result[w]


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    # 그래프 및 진입차수 초기화
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    data = list(map(int, input().split()))

    # 간선 정보 입력
    for _ in range(m):
        a, b = map(int, input().split())
        # a -> b
        graph[a].append(b)
        indegree[b] += 1

    w = int(input())
    print(topology_sort(data, w))