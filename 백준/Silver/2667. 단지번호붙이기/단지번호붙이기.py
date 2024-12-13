# 아이디어: 1. bfs 알고리즘을 이용해 단지 수 파악
#           2. 아파트 단지 수 오름차순 정렬
# 알고리즘: bfs
# 자료구조: queue(deque)

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(x, y):
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 해당 지점에 아파트가 있다면
            if graph[nx][ny] == 1:
                cnt += 1
                graph[nx][ny] = 0
                queue.append((nx, ny))

    return cnt

apts = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = bfs(i, j)
            apts.append(cnt)

apts.sort()

print(len(apts))
for x in apts:
    print(x)