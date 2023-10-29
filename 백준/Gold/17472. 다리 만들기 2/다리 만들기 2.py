# 아이디어: 1. bfs로 각 구역 다른 숫자로 나누기 (visited 테이블 선언)
# 알고리즘: MST, kruskal, bfs
# 자료구조: queue

from collections import deque
import sys
input = sys.stdin.readline

# bfs 함수 정의
def bfs(x, y, mark):
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = mark
    
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            # 현재 지점이 바다이거나 방문한 적이 있다면 무시
            if graph[nx][ny] == 0 or visited[nx][ny]:
                continue
            
            # 다른 숫자로 변경
            graph[nx][ny] = mark
            visited[nx][ny] = True
            queue.append((nx, ny))
            
# 간선 가중치 함수 정의
def getEdges(x, y, now):
    # 큐 및 시작노드 정의
    queue = deque()
    for i in range(4):
        queue.append((x, y, 0, i)) # (x, y, 가중치, 4방향)
        
    # 큐가 빌 때까지
    while queue:
        x, y, cost, i = queue.popleft()

        # 현재 위치가 바다가 아니면서 동일 섬이 아니라면
        if graph[x][y] != 0 and graph[x][y] != now:
            # 다리의 길이가 2이상(현재 지점까지 포함해서 2보다 클 때)
            if cost > 2:
                edges.append((cost-1, now, graph[x][y]))
            continue
        
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 범위 밖이라면 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        
        # 다음 지점이 같은 섬이라면 무시
        if graph[nx][ny] == now:
            continue
            
        queue.append((nx, ny, cost + 1, i))
        
# find 함수 정의(경로 압축)
def find(x):
    # 루트 노드가 아니라면
    if parent[x] != x :
        parent[x] = find(parent[x])
        
    return parent[x]

# union 함수 정의
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

# 그래프 정보 입력 visited 테이블 선언
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mark = 1 # 현재 칠할 섬의 숫자
for i in range(n):
    for j in range(m):
        # 현재 지점이 땅이면서 방문한 적이 없다면
        if graph[i][j] == 1 and not visited[i][j]:
            bfs(i, j, mark)
            mark += 1

# 간선 테이블 정의
edges = []

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            getEdges(i, j, graph[i][j])
            
# 간선에 대한 중복 제거하기 (같은 거리 처리)
edges = list(set(edges))

# 간선 오름차순 정렬
edges.sort()

# parent 테이블 선언
parent = [i for i in range(mark)]

result = 0 # 가중치 총 비용
cnt = 0 # 간선 개수

for cost, a, b in edges:
    # 사이클이 아니라면
    if find(a) != find(b):
        union(a, b)
        result += cost
        cnt += 1
        
# 가중치가 없거나 다리의 개수가 (섬-1)보다 작다면
# mark는 섬 + 1
if result == 0 or cnt != mark - 2:
    print(-1)
else:
    print(result)