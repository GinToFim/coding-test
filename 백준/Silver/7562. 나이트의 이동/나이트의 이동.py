# 아이디어 : 1. 나이트의 8방향 정의
#            2. 방문 여부를 위한 graph 0으로 초기화
# 알고리즘 : bfs
# 자료구조 : queue(deque)

# 시작지점 - (x, y), 도착지점 - (p, q)

from collections import deque
import sys
input = sys.stdin.readline

# bfs 함수 정의
def bfs(x, y):
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append((x, y, 0))
    graph[x][y] = 1
    
    while queue:
        x, y, cnt = queue.popleft()
        
        # 도착 지점이라면
        if x == p and y == q :
            return cnt
        
        for step in steps:
            nx = x + step[0]
            ny = y + step[1]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
                
            # 방문한 적이 없다면
            if graph[nx][ny] == 0 :
                graph[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))

# 나이트의 이동 8방향 정의
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1),
         (-1, -2), (-1, 2), (1, -2), (1, 2)]

T = int(input())

for _ in range(T):
    n = int(input())
    x, y = map(int, input().split())
    p, q = map(int, input().split())

    graph = [[0 for _ in range(n)] for _ in range(n)]

    print(bfs(x, y))