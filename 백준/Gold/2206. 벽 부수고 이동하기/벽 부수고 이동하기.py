# 아이디어 : 1. short_path에 해당하는 3차원 리스트를 선언
#              (마지막 차원이 벽 부수기에 해당)
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

# bfs 함수 선언 
def bfs(x, y) :

    # 큐 및 시작노드 선언
    queue = deque()
    queue.append((x, y, 0)) # (x, y, 벽)
    visited[x][y][0] = 1

    while queue :
        x, y, block = queue.popleft()

        # 도착했다면 break
        if x == n-1 and y == m-1 :
            return visited[x][y][block]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이라면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue

            # 다음이 이동할 수 있는 곳이라면서(0) 아직 한 번도 방문하지 않았다면
            if graph[nx][ny] == 0 and not visited[nx][ny][block]:
                visited[nx][ny][block] = visited[x][y][block] + 1
                queue.append((nx, ny, block))

            # 다음이 벽이면서(1) 아직 벽을 부실 기회가 남았다면
            if graph[nx][ny] == 1 and block == 0 :
                visited[nx][ny][1] = visited[x][y][block] + 1
                queue.append((nx, ny, 1))
            
    # 끝지점에 도착하지 못했다면
    return -1

result = bfs(0, 0)
print(result)