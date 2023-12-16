from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [] # 그래프 초기화
data = [] # 바이러스에 대한 정보를 담을 리스트

for i in range(n) :
	graph.append(list(map(int, input().split())))
	for j in range(n) :
		# 해당 위치에 바이러스 존재하는 경우
		if graph[i][j] != 0 :
			# (바이러스 레벨, 시간, x, y) 저장
			data.append((graph[i][j], 0, i, j))

# 오름차순 정렬 이후에 큐로 옮기기
data.sort()
queue = deque(data)

S, X, Y = map(int, input().split())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 알고리즘
while queue :
	virus, sec, x, y = queue.popleft()

	# S초를 지나거나 큐가 빌 때까지 실행
	if sec == S :
		break

	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]

		# 범위 밖일 경우
		if nx < 0 or ny < 0 or nx >= n or ny >= n :
			continue

		if graph[nx][ny] == 0 :
			graph[nx][ny] = virus 
			queue.append((virus, sec + 1, nx, ny))

print(graph[X-1][Y-1])		