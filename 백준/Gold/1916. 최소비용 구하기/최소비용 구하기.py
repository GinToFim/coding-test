import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
# 거리 테이블 초기화
distance = [INF] * (n + 1)

# 간선 입력
for _ in range(m) :
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

start, end = map(int, input().split())
	
# 다익스트라 알고리즘 정의
def dijkstra(start) :
	# 시작 노드 정의
	hq = []
	heapq.heappush(hq, (0, start)) #(거리, 노드)
	distance[start] = 0

	# hq가 빌 때까지
	while hq :
		dist, now = heapq.heappop(hq)
		# 이미 거친 적이 있으면 무시
		if distance[now] < dist :
			continue

		# v - (노드, 거리)
		for v in graph[now] :
			cost = dist + v[1]
			if cost < distance[v[0]] :
				distance[v[0]] = cost
				heapq.heappush(hq, (cost, v[0]))

dijkstra(start)

print(distance[end])