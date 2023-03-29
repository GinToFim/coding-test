from collections import deque

n, k = map(int, input().split())
graph = [-1] * (100001)

def bfs(start) :
	# 시작노드 초기화
	graph[start] = 0
	queue = deque()
	queue.append(start)

	while queue :
		x = queue.popleft()
		nx_list = []
		nx_list.append(x-1)
		nx_list.append(x+1)
		nx_list.append(x*2)

		for nx in nx_list :
			if nx <= -1 or nx >= 100001 :
				continue

			if graph[nx] == -1 :
				graph[nx] = graph[x] + 1
				queue.append(nx)
				
bfs(n)
print(graph[k])