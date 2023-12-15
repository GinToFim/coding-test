# 아이디어: 1. 빈칸(0)인 구역을 기억 후 3개를 조합으로 뽑기
#           2. 조합으로 뽑은 후 해당 구역을 벽(1)으로 바꾸기
#           3. 바이러스(2)를 퍼지게 한 후(bfs) 안전 구역(0)의 개수 구하기
#           4. 위 과정들을 완전 탐색
# 알고리즘: bfs, 완전 탐색, 조합
# 자료구조: queue(deque)

from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

# bfs 알고리즘 정의하기
def bfs(graph):
    # 큐 및 시작 노드 정의 (바이러스(2)인 곳 모두 추가)
    queue = deque(virus_spaces)
    
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
                
            # 만약 해당 지역이 빈 곳(0)이라면 추가하기
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2 # 바이러스로 변경
                queue.append((nx, ny))
                
    # 안전 구역(0)인 곳 카운트하기
    safe_count = 0
    for row in graph:
        safe_count += row.count(0)
        
    return safe_count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 정의하기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈 공간 및 바이러스 공간 기억하기
empty_spaces = []
virus_spaces = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_spaces.append((i, j))
            
        if graph[i][j] == 2:
            virus_spaces.append((i, j))
    
result = 0
    
# 조합으로 3개 뽑기 2행 1열, 1행 2열, 4행 6
for iter_case in combinations(empty_spaces, 3):
# iter_case = [(1, 0), (0, 1), (3, 5)]
    new_graph = copy.deepcopy(graph)

    # 해당 구역 벽(1)으로 바꾸기
    for x, y in iter_case:
        new_graph[x][y] = 1
    
    safe_count = bfs(new_graph)
    result = max(result, safe_count) # 안전 구역 개수 갱신 

print(result)