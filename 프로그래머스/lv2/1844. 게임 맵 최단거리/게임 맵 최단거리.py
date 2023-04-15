# 아이디어 : 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냄
# 알고리즘 : bfs(graph, dx/dy)
# 자료구조 : queue(deque)

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append((0, 0))
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue
            
            # 지나갈 수 있다면 (1)
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1 :
        return -1  
    else :
        return maps[n-1][m-1]