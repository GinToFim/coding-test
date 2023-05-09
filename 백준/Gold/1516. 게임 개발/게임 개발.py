# 아이디어 : 1.
# 알고리즘 : topology sort(graph, indegree)
# 자료구조 : deque(queue)

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
times = [-1]  # 해당 노드만 걸리는 시간
result = [-1]  # 총 걸리는 시간
indegree = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    t = data[0]
    times.append(t)
    result.append(t)

    for x in data[1:-1]:
        # x -> i
        graph[x].append(i)
        indegree[i] += 1

# 큐 정의
queue = deque()

# 진입차수가 0인 노드 append
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

# 큐가 빌 때까지
while queue:
    now = queue.popleft()

    # 해당 노드와 인접한 노드들 시간 추가, 진입차수 1씩 빼기
    for v in graph[now]:
        result[v] = max(result[v], result[now] + times[v])
        indegree[v] -= 1

        # 진입차수가 0이라면
        if indegree[v] == 0:
            queue.append(v)

for x in result[1:]:
    print(x)