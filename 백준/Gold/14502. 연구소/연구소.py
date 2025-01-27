import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split()))
        for _ in range(n)]

# 상하좌우 선언
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스와 빈 칸 기억하기
starts = []
blanks = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            starts.append((i, j))

        if graph[i][j] == 0:
            blanks.append((i, j))


combinations = []
now = []

def dfs(depth, start):
    # 종료 조건
    if depth == 3:
        combinations.append([x for x in now])
        return
    
    for i in range(start, len(blanks)):
        now.append(blanks[i])
        dfs(depth + 1, i + 1)
        now.pop()

dfs(0, 0)

result = -1


for iter_case in combinations:
    copy_graph = [row[:] for row in graph]

    # 벽 새로 세우기
    for x, y in iter_case:
        copy_graph[x][y] = 1

    # 시작 노드 및 큐 선언
    queue = deque()
    for start in starts:
        queue.append(start)

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 현재 위치가 빈 칸이라면
            if copy_graph[nx][ny] == 0:
                # 바이러스로 변경
                copy_graph[nx][ny] = 2
                queue.append((nx, ny))
        
    safe_cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 0:
                safe_cnt += 1

    result = max(result, safe_cnt)

print(result)