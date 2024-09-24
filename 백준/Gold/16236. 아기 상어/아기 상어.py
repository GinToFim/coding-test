# 아이디어:
# 알고리즘: bfs
# 자료구조: queue(deque)

from collections import deque
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# dx, dy 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어의 현재 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0
            break

# 아기 상어의 레벨과, 현재 먹은 양
level = 2
now_ate = 0

result = 0

def bfs(now_x, now_y):
    # 방문 테이블 선언
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((now_x, now_y))
    visited[now_x][now_y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
        
            # 방문한 적이 없으면서, 아기 상어가 지나갈 수 있다면
            if visited[nx][ny] == -1 and graph[nx][ny] <= level:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    return visited

# 최소 거리이면서 먹을 수 있는 물고기 탐색
def find(visited):
    min_dist = INF

    for i in range(n):
        for j in range(n):
            # 물고기이고 아기상어보다 작으면서, 지나갈 수 있다면
            if 1 <= graph[i][j] < level and visited[i][j] != -1:
                dist = visited[i][j]

                # 거리가 기존 거리보다 작다면, 갱신
                if dist < min_dist:
                    x, y = i, j
                    min_dist = dist
    
    # 더 이상 지나갈 수 없다면
    if min_dist == INF:
        return None

    return min_dist, x, y

while True:
    # 먹을 수 있는 물고기 찾기
    visited = bfs(now_x, now_y)
    value = find(visited)

    # 더 이상 먹을 물고기가 없다면
    if value == None:
        print(result)
        break

    min_dist, x, y = value

    
    # 아기 상어의 위치 및 결과 거리 갱신
    now_x, now_y = x, y
    result += min_dist
    now_ate += 1

    # 물고기를 먹은 위치에 아무것도 없도록 설정
    graph[now_x][now_y] = 0

    # 아기상어가 커질 수 있다면
    if level <= now_ate:
        level += 1
        now_ate = 0
