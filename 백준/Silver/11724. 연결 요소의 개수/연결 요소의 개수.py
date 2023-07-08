from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m) :
	a, b = map(int, input().split())
	graph[a][b] = 1
	graph[b][a] = 1

def bfs(graph, start, visited) :
	# 시작노드 정의
	queue = deque()
	queue.append(start)
	visited[start] = True

	# 큐가 빌 때까지
	while queue :
		v = queue.popleft()
		for i in range(1, n + 1) :
			if not visited[i] and graph[v][i] == 1:
				queue.append(i)
				visited[i] = True

result = 0 # 연결 요소 개수
for i in range(1, n + 1) :
	if not visited[i] :
		bfs(graph, i, visited)
		result += 1

print(result)