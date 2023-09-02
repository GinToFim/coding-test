# 아이디어 : 1. 그래프, 상하좌우, 큐 정의
#            2. bfs 탐색을 통하여 연결되어 있는 단지수 탐색
#            3. 탐색된 단지수 오름차순 정렬
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

# 그래프 입력
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs(x, y):
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1 # 연결되는 아파트의 수
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
                
            # 아파트(1)라면
            if graph[nx][ny] == 1 :
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    
    return cnt

# 단지의 아파트 수 리스트
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            cnt = bfs(i, j)
            result.append(cnt)

# 오름차순 정렬
result.sort()

print(len(result))
for x in result :
    print(x)