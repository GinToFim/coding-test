# 아이디어 : 1. 벽 3개를 세우기(combinations 사용)
#            2. bfs를 사용하여 바이러스가 퍼지는 것 확인하기
#            3. 안전 지역(0) max 값 구하기
# 알고리즘 : bfs, combinations (64C3 -> 2^18 = )
# 자료구조 : queue(deque)

# 빈 칸(0), 벽(1), 바이러스(2)

import copy
from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

safe_areas = [] # 빈칸 위치 
virus_areas = [] # 바이러스 위치
for i in range(n) :
    for j in range(m) :
        if graph[i][j] == 0:
            safe_areas.append((i, j))
        
        if graph[i][j] == 2 :
            virus_areas.append((i, j))

# bfs 정의하기
def bfs(graph) :
    # 시작노드 및 큐 정의
    queue = deque(virus_areas)
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            
            # 다음 지역이 빈칸이라면 바이러스 노출
            if graph[nx][ny] == 0 :
                graph[nx][ny] = 2
                queue.append((nx, ny))

    
result = 0
    
# 조합으로 빈칸 위치 3개 뽑기 (벽으로 변경)
for change_walls in combinations(safe_areas, 3) :
    tmp_graph = copy.deepcopy(graph)
    
    # 3개의 점만 벽으로 변경하기
    for a, b in change_walls :
        tmp_graph[a][b] = 1 
        
    # bfs 실행
    bfs(tmp_graph)
    
    # 안전 지역 개수 세기
    cnt = 0
    for row in tmp_graph :
        cnt += row.count(0)
    
    result = max(result, cnt)
    
print(result)