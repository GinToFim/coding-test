import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().rstrip())))

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
	global cnt 
	graph[x][y] = 0
	cnt += 1

	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]

		if nx <= -1 or nx >=n or ny <= -1 or ny >= n :
			continue
		if graph[nx][ny] == 1 : 
			dfs(nx, ny)
   

result = 0 # 아파트 단지 수
apt = [] # 아파트 단지 array

for i in range(n) :
	for j in range(n) :
		if graph[i][j] == 1:
			cnt = 0 # 아파트 단지당 개수
			dfs(i, j)
			apt.append(cnt)
			result += 1


apt.sort()
print(result)
for x in apt :
    print(x)