from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 그래프 초기화

for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)

# 거리 테이블 초기화 ('-1'로 방문 여부 체크)
distance = [-1] * (n + 1)
distance[x] = 0 # 시작노드 거리 0으로 초기화

# BFS 수행
queue = deque()
queue.append(x) # 시작노드 초기화

# 큐가 빌 때까지
while queue :
	now = queue.popleft()

	for v in graph[now] :
		if distance[v] == -1 :
			distance[v] = distance[now] + 1
			queue.append(v)

# 최단 거리가 K인 모든 도시의 번호를 오름차순 출력
check = False
for i in range(1, n + 1) :
	if distance[i] == k :
		print(i)
		check = True

# 만약 최단 거리가 K인 도시가 없다면 -1 출력
if not check :
	print(-1)