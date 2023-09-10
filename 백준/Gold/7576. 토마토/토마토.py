# 아이디어 : 1. 그래프 및 상하좌우 정의
#            2. 시작지점이 여러 개 (queue)
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs():
    # 시작노드 및 큐 정의
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 :
                queue.append((i, j))
    
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
                
            if graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    max_value = -100
    
    for i in range(n):
        for j in range(m):
            # 익지 않은 토마토가 있다면
            if graph[i][j] == 0 :
                return -1
            
            # 최댓값 갱신
            if graph[i][j] > max_value :
                max_value = graph[i][j]
    
    # 박스에 토마토가 하나도 없다면
    return max_value - 1

print(bfs())