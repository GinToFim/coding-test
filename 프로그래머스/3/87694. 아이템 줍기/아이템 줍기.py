# 아이디어: 1. 직사각형의 테두리만 지나가도록 표시
#          2. 각 좌표를 2배로 늘리기
# 알고리즘: bfs
# 자료구조: queue(deque)

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[0 for _ in range(102)] for _ in range(102)]
    
    # dx, dy 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    
    # 좌표 2배로 늘리기
    rectangle = [(2*x1, 2*y1, 2*x2, 2*y2) for x1, y1, x2, y2 in rectangle]
    cx, cy = 2*characterX, 2*characterY
    ix, iy = 2*itemX, 2*itemY
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                # 사각형의 내부라면
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 0
                # 사각형의 테두리이면서, 다른 사각형가 아니라면
                elif graph[x][y] != 0:
                    graph[x][y] = 1
    
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((cx, cy))

    
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        # 현재 지점이 도착 지점이라면
        if (x, y) == (ix, iy):
            return visited[x][y] // 2
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 현재 지점이 테두리 위면서 한 번도 방문한 적이 없다면
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                

    return answer