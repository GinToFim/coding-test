# 아이디어: 
# 알고리즘: bfs
# 자료구조: queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

# bfs 알고리즘 정의
def bfs(x, y):
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append((x, y))
    
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 지나갈 수 있는 곳이라면
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

n, m = map(int, input().split())

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().rstrip())) for _ in range(n)]

print(bfs(0, 0))