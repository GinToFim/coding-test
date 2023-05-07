import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# 정점, 간선 입력
n, e = map(int, input().split())
graph = [[] for i in range(n+1)]

# 간선 정보 입력
for _ in range(e) :
	a, b, c = map(int, input().split())
	# 양방향
	graph[a].append((b, c))
	graph[b].append((a, c))

# 두 정점 입력
v1, v2 = map(int, input().split())

def dijkstra(start, end) :
	# 거리 재정의
	distance = [INF] * (n + 1)
	# 시작노드 & heapq 정의
	hq = []
	heapq.heappush(hq, (0, start))
	distance[start] = 0

	while hq :
		dist, now = heapq.heappop(hq)
		# 이미 처리된 적이 있으면 무시
		if distance[now] < dist :
			continue

		for v in graph[now] :
			cost = dist + v[1]
			if cost < distance[v[0]] :
				distance[v[0]] = cost
				heapq.heappush(hq, (cost,v[0]))

	return distance[end]

value1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
value2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

result = min(value1, value2)
print(result if result < INF else -1)