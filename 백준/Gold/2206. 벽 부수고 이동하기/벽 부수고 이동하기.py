# 아이디어 : 1. 벽을 한 번 뚫었는지 여부를 3차원으로 구별
#           2. 무조건 방문했다고 그곳을 무시하면 안됨 why? 
# 알고리즘 : bfs (graph, deque, 상하좌우, visited)
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n) :
    graph.append(list(map(int, input().rstrip())))
    

# 벽과는 따로 기록하기 위해서(x, y) + 벽을 뚫었는지 여부 체크(z)
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

def bfs(x, y, z) :
   # 큐 및 시작노드 정의
    queue = deque()
    queue.append((0, 0, 0)) 
    visited[0][0][0] = 1
    
    # 큐가 빌 때까지
    while queue :
        x, y, block = queue.popleft()

        # 도착지 도착했으면 return
        if x == n-1 and y == m-1 :
            return visited[x][y][block]
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            # 벽이 뚤려있고, 아직 한 번도 방문하지 않았으면
            if graph[nx][ny] == 0 and visited[nx][ny][block] == 0 :
                queue.append((nx, ny, block))
                visited[nx][ny][block] = visited[x][y][block] + 1
            
            # 벽이 막혀있는데 아직 한 번도 안뚤었으면
            if graph[nx][ny] == 1 and block == 0 :
                queue.append((nx, ny, 1))
                visited[nx][ny][1] = visited[x][y][block] + 1
    
    # 도착하지 않았다면
    return -1

print(bfs(0, 0, 0))