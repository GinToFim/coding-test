# 아이디어 : 1. bfs(start, end)로 선언
#          2. bfs((start), (lever)) + bfs((lever), (end))

# 알고리즘 : bfs(graph, dx/dy)
# 자료구조 : deque(queue)

from collections import deque

def solution(maps):
    answer = 0
    n = len(maps) # 행의 길이
    m = len(maps[0]) # 열의 길이
    
    # 상하좌우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    start, end, lever = (0, 0), (0, 0), (0, 0)
    
    # start, end, lever의 위치 저장하기
    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 'S' :
                start = (i, j)
            
            if maps[i][j] == 'E' :
                end = (i, j)
            
            if maps[i][j] == 'L' :
                lever = (i, j)
    
    # 출발지, 목적지
    def bfs(start, end) :
        # 방문지 초기화
        visited = [[-1] * m for _ in range(n)]
        sx, sy = start
        ex, ey = end
        
        print(start, end)
        
        # 큐 및 시작노드 정의
        queue = deque()
        queue.append((sx, sy))
        visited[sx][sy] = 0
        
        # 큐가 빌 때까지
        while queue :
            x, y = queue.popleft()
            
            # 목적지에 도착했다면
            if x == ex and y == ey :
                return visited[x][y]
            
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 밖이라면 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m :
                    continue
            
                # 지나갈 수 있는 곳이고 아직 방문하지 않았다면
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1 :
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        
        # 목적지에 도착할 수 없다면
        return -1
    
    first = bfs(start, lever)
    second = bfs(lever, end)
    
    if first == -1 or second == -1 :
        return -1
    else :
        return first + second
