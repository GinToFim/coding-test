# 아이디어 : 1. bfs로 지나갈 수 있는지 확인 
#           2. bfs 함수는 각 위치에 대한 최단거리 구하기
#           3. find 함수는 아기 상어가 갈 최소 거리의 위치를 구함
# 알고리즘 : bfs(graph, dx/dy)
# 자료구조 : queue(deuqe)

from collections import deque
import sys
input = sys.stdin.readline
INF = 1e9

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 아기 상어 위치 및 크기
now_x, now_y = 0, 0
now_size = 2

# 아기 상어 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0 # 지나가게 만들기 위해 0으로
            break

    
# 다른 상어와 아기 상어의 거리
def bfs(now_x, now_y):
    # 거리 테이블 초기화
    dist = [[-1] * n for _ in range(n)]
    
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((now_x, now_y))
    dist[now_x][now_y] = 0
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 이내라면
            if (0 <= nx < n) and (0 <= ny < n):
                # 한 번도 방문한 적이 없고
                # 아기상어가 지나갈 수 있다면
                if dist[nx][ny] == -1 and graph[nx][ny] <= now_size :
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    
    return dist

# 아기 상어과 갈 위치 (최소 거리)
def find(dist):
    x, y = 0, 0 # 다른 상어 위치
    min_dist = INF # 최소 거리

    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 아기 상어가 먹을 수 있는 상어일 때
            if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
                # 가장 가까우면 갱신 (행렬 우선)
                if dist[i][j] < min_dist :
                    x, y = i, j
                    min_dist = dist[i][j]

    # 도달할 최소 위치가 없다면
    if min_dist == INF :
        return None
    else :
        return x, y, min_dist

result = 0 # 버틴 시간
ate = 0 # 먹은 상어 수
    
while True :
    dist = bfs(now_x, now_y)
    value = find(dist)     
    
    if value == None:
        print(result)
        break
    else :
        x, y, min_dist = value
        
        # 버틴 시간 갱신
        result += min_dist
        ate += 1
        
        # 아기 상어 위치 갱신
        now_x, now_y = x, y
        
        # 그 위치는 상어가 없도록
        graph[now_x][now_y] = 0
        
        # 크기 업이 가능하다면
        if ate >= now_size:
            now_size += 1
            ate = 0
    