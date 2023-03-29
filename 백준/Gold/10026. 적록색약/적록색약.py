# 아이디어 : 1. 적록색약(빨강 == 초록)
# 알고리즘 : bfs (graph, 상하좌우, deque)
# 자료구조 : deque

from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(graph, x, y, color) :
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((x, y))
    graph[x][y] = '0'
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            
            if graph[nx][ny] == color :
                graph[nx][ny] = '0'
                queue.append((nx, ny))

n = int(input())
graph = []
for _ in range(n) :
    graph.append(list(input().rstrip()))

# R을 G로 변경(적록색약)
cw_graph = copy.deepcopy(graph)
for i in range(n) :
    for j in range(n) :
        if cw_graph[i][j] == 'R' :
            cw_graph[i][j] = 'G'
    
# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                
normal = 0
for i in range(n) :
    for j in range(n) :
        if graph[i][j] in 'RGB' :
            bfs(graph, i, j, graph[i][j])
            normal += 1

cw = 0
for i in range(n) :
    for j in range(n) :
        if cw_graph[i][j] in 'GB' :
            bfs(cw_graph, i, j, cw_graph[i][j])
            cw += 1
            
print(normal, cw)