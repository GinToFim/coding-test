# 아이디어:
# 알고리즘: 구현, 시물레이션

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = [list(map(int, input().split()))
        for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

while True:
    # 현재 위치를 한 번도 방문한 적이 없다면
    if not visited[x][y]:
        # 현재 위치 방문 처리
        visited[x][y] = True
        result += 1

    # 다음 칸 탐색하기
    for _ in range(4):
        d = (d-1) % 4
        # 다음 칸 확인하기
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 밖이라면 무시하기
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        # 방문한 적이 없으면서, 갈 수 있는 곳이라면
        if not visited[nx][ny] and graph[nx][ny] == 0:
            x, y = nx, ny
            break

    # 다음 위치로 갈 곳이 없다면
    else:
        # 뒤로 이동하기
        nx = x - dx[d]
        ny = y - dy[d]

        # 범위 안이면서 뒤로 갈 수 있다면
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            x, y = nx, ny
        else:
            print(result)
            break