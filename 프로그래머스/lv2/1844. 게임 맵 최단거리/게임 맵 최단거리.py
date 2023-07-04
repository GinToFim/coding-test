# 아이디어 : 1. 행과 열 크기 및 상하좌우 선언
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((0, 0))
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위를 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
                
            # 미로가 이동이 가능하다면
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1 :
        return -1
    else :
        return maps[n-1][m-1] 
