# 아이디어 :
# 알고리즘 : bfs (graph, dx/dy)
# 자료구조 : queue(deque)

from collections import deque
import sys

input = sys.stdin.readline
INF = 1e9

# 맵의 크기 입력
n = int(input())

# 상어들에 정보 입력
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어 정보(현재 크기, 위치)
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 위치를 찾은 뒤에 0으로 변경
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0
            break


# 모든 위치까지의 '최단 거리'만 구하는 함수
# 아기 상어가 움직일 수 있는지 체크하기 위하여 bfs 사용
def bfs():
    # 값이 -1이라면 통과할 수 없다는 의미
    dist = [[-1 for _ in range(n)] for _ in range(n)]

    # 큐 및 시작노드(아기상어) 정의
    queue = deque()
    queue.append((now_x, now_y))
    dist[now_x][now_y] = 0

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 이내라면
            if 0 <= nx < n and 0 <= ny < n:
                # 방문한 적이 없고
                # 자신이 크기보다 작거나 같은 경우에 움직일 수 있음
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return dist


# 최단 거리 테이블이 주어졌을 때, 먹을 물고기 찾는 함수
def find(dist):
    x, y = 0, 0  # 물고기 위치
    min_dist = INF  # 물고기의 최소 거리

    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                # 가장 가까운 물고기 한 마리만 선택 (행 우선, 열 우선)
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]

    # 물고기를 먹을 수 없는 경우
    if min_dist == INF:
        return None
    # 먹을 수 있는 경우
    else:
        return x, y, min_dist


result = 0  # 버틴 시간
ate = 0  # 현재 크기에서 먹은 물고기

while True:
    # 먹을 수 있는 물고기 찾기
    dist = bfs()
    value = find(dist)

    if value == None:
        print(result)
        break
    else:
        x, y, dist = value

        # 아기 상어의 현재 위치 갱신
        now_x, now_y = x, y
        result += dist

        # 먹은 위치에는 아무것도 없도록 처리
        graph[now_x][now_y] = 0
        ate += 1

        # 크기가 커질 수 있다면
        if ate >= now_size:
            now_size += 1
            ate = 0