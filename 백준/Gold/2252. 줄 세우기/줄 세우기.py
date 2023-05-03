from collections import deque
import sys
input = sys.stdin.readline

# 노드, 간선 개수 입력
v, e = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(v + 1)]
# 진입차수 초기화
indegree = [0] * (v + 1)

# 간선 정보 입력
for _ in range(e) :
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1

def topology_sort() :
	result = [] # 수행 결과 리스트
	queue = deque()

	# 진입 차수가 0인 노드 추가
	for i in range(1, v + 1) :
		if indegree[i] == 0 :
			queue.append(i)

	# 큐가 빌 때까지
	while queue :
		now = queue.popleft()
		result.append(now)

		for i in graph[now] :
			indegree[i] -= 1
			if indegree[i] == 0 :
				queue.append(i)

	# 결과 출력
	for x in result :
		print(x, end=' ')

topology_sort()