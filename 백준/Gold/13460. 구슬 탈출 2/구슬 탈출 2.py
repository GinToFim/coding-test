from collections import deque

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[[False for _ in range(m)] for _ in range(n)]
            for _ in range(m)] for _ in range(n)]

# 한 쪽 방향으로만 가는 함수 정의
def move_end(x, y, i):
    cnt = 0 # 이동한 칸의 횟수

    while True:
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

# bfs 함수 정의
def bfs(rx, ry, bx, by):
    # 큐 및 시작 노드 정의
    queue = deque()
    queue.append((rx, ry, bx, by, 1)) #(빨간 구슬, 파란 구슬, 이동 횟수)
    visited[rx][ry][bx][by] = True

    # 큐가 빌 때까지
    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        # 이미 이동 횟수가 10번 이상이라면
        if depth > 10:
            return -1
        
        for i in range(4):
            # 빨간 구슬, 파란 구슬 이동
            nrx, nry, rcnt = move_end(rx, ry, i)
            nbx, nby, bcnt = move_end(bx, by, i)

            # 파란 구슬이 구멍에 도착했다면 (빨간 구슬 동시에 도착 포함)
            if graph[nbx][nby] == 'O':
                continue

            # 빨간 구슬만 도착했다면
            if graph[nrx][nry] == 'O':
                return depth
            
            # 같은 지점에 2개의 구슬이 있다면
            if (nrx, nry) == (nbx, nby):
                # 많이 이동한 구슬을 한 칸 빼기
                if rcnt > bcnt:
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            # 두 개의 구슬이 한 번도 방문한 적이 없다면
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))

    # 아무것도 도착하지 않았다면
    return -1

# 빨간 구슬, 파란 구슬 위치 기억
rx, ry, bx, by = -1, -1, -1, -1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R':
            rx, ry = i, j
            graph[i][j] = '.'
        
        if graph[i][j] == 'B':
            bx, by = i, j
            graph[i][j] = '.'

result = bfs(rx, ry, bx, by)
print(result)