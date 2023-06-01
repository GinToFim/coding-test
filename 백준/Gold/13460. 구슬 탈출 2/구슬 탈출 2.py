# 아이디어 : 1. visited table 4차원으로 구성(rx, ry, bx, by 위치 기억)
#           2. move #(벽), O(구멍)일 때까지 움직이기
#           3. bfs 구현 (빨강, 파랑 동시에 빠지면 X)
# 알고리즘 : bfs + implemenation
# 자료구조 : queue(deque)

# 가장자리가 모두 벽이라서 범위 체크 필요 X

from collections import deque
import sys
input = sys.stdin.readline

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 한쪽 방향으로만 가게 설정
def move(x, y, i):
    cnt = 0 # 이동한 칸 수
    
    while True :
        nx = x + dx[i]
        ny = y + dy[i]
        cnt += 1
        
        # 이동한 곳이 벽이라면 (한 칸 빼기)
        if graph[nx][ny] == '#':
            return x, y, cnt - 1
        
        # 이동한 곳이 구멍이라면
        if graph[nx][ny] == 'O':
            return nx, ny, cnt
        
        x, y = nx, ny

def bfs(rx, ry, bx, by):
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    
    while queue :
        rx, ry, bx, by, depth = queue.popleft()
        
        # 보드의 움직임이 10번을 넘어가면
        if depth > 10 :
            return -1
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)
            
            # 파란 구슬이 구멍에 도착했다면(빨간 구슬과 동시 도착도 포함)
            if graph[nbx][nby] == 'O':
                continue
            
            # 빨간 구슬만 구멍에 도착했다면
            if graph[nrx][nry] == 'O':
                return depth
            
            # 같은 지점에 2개의 구슬이 있다면
            if (nrx, nry) == (nbx, nby):
                # 많이 이동한 구슬 한 칸 빼기
                if rcnt > bcnt :
                    nrx -= dx[i]
                    nry -= dy[i]
                else :
                    nbx -= dx[i]
                    nby -= dy[i]
            
            # 두 개 구슬 모두 한 번도 방문한 적이 없다면
            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    
    return -1
            
            
            
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(n)]

    # visited 테이블 선언
    visited = [[[[False] * m for _ in range(n)]
                   for _ in range(m)] for _ in range(n)]

    
    # 빨간, 파란 구슬 위치 기억
    rx, ry, bx, by = -1, -1, -1, -1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = (i, j)
                graph[i][j] = '.'
            
            if graph[i][j] == 'B':
                bx, by = (i, j)
                graph[i][j] = '.'
                
    result = bfs(rx, ry, bx, by)
    print(result)
            