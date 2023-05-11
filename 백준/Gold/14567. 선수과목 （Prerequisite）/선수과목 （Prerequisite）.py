# 아이디어 : 선수과목에 해당하는 과목마다 1씩 더하기
# 알고리즘 : topology sort(graph, indegree)
# 자료구조 : queue(deque)

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
# 진입 차수 초기화
indegree = [0 for _ in range(n + 1)]

# 학기 리스트
times = [1 for _ in range(n + 1)]
# 학기 총합 리스트
result = [1 for _ in range(n + 1)]

# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    # a -> b
    graph[a].append(b)
    indegree[b] += 1

# 진입차수가 0인 노드 큐에 추가
queue = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

# 큐가 빌 때까지
while queue:
    now = queue.popleft()

    # 해당 노드와 인접한 노드들 확인
    for v in graph[now]:
        result[v] = max(result[v], result[now] + times[v])
        indegree[v] -= 1

        # 진입차수가 0이라면
        if indegree[v] == 0:
            queue.append(v)

print(*result[1:])