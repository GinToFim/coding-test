# 아이디어 : 1. bfs를 1방이 아닌 4방으로?
# 알고리즘 : bfs
# 자료구조 : queue(deque)

# '.'은 빈 칸, '#'은 벽, 'O'는 구멍의 위치
# 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치

from collections import deque
import sys
input = sys.stdin.readline

def move(x, y, i):
    cnt = 0
    
    while True:
        cnt += 1
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 이동할 위치가 구멍이라면
        if board[nx][ny] == 'O':
            return nx, ny, cnt
        
        # 이동할 위치가 벽이라면 (그전으로 이동)
        if board[nx][ny] == '#':
            return x, y, cnt - 1
        
        x, y = nx, ny
    

# bfs 알고리즘 정의
def bfs(rx, ry, bx, by):
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    
    # 큐가 빌 때까지
    while queue :
        rx, ry, bx, by, depth = queue.popleft()
        
        # 방향이 10번을 넘어가면
        if depth > 10 :
            continue
        
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, i)
            nbx, nby, bcnt = move(bx, by, i)
            
            # 파란 구슬이 구멍에 도착하면 실패 (동시에 도착한 경우도 포함)
            if board[nbx][nby] == 'O' :
                continue
            
            # 빨간 구슬만 도착하면 성공 (가장 빨리 도착하면 바로 끝냄)
            if board[nrx][nry] == 'O' :
                return depth

            # 빨간 구슬과 파란 구슬이 겹쳤다면, 많이 움직인 구슬 한 칸 빼기
            if nrx == nbx and nry == nby :
                if rcnt > bcnt :
                    nrx -= dx[i]
                    nry -= dy[i]
                else :
                    nbx -= dx[i]
                    nby -= dy[i]

            # 한 번도 방문한 적이 없다면     
            if not visited[nrx][nry][nbx][nby] :
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    
    return -1

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# visited 테이블 만들기 (4차원 테이블)
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

# 빨간 구슬, 파란 구슬 위치 초기화
rx, ry, bx, by = -1, -1, -1, -1

# 빨간 구슬, 파랑 구슬 위치 찾기
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        
        if board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'
    
result = bfs(rx, ry, bx, by)
print(result)