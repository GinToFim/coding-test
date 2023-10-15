# 아이디어: 1. 임의의 정점(1)에서 가장 먼 정점(y) 구하기
#           2. 정점 y에서 가장 먼 정점 z 구하기
#           3. y와 z 사이의 거리가 트리의 지름이다.
# 알고리즘: tree, dfs

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# dfs 정의
def dfs(x, cost):
    for y, w in graph[x]:
        # 방문한 적이 없다면
        if distance[y] == -1 :
            distance[y] = cost + w
            dfs(y, cost + w)

n = int(input())
graph = [[] for _ in range(n + 1)]

# 트리 입력받기
for _ in range(n):
    data = list(map(int, input().split()))
    v = data[0]
    
    for i in range(1, len(data)-1, 2):
        graph[v].append((data[i], data[i+1])) # (노드, 가중치) 형태

# 거리 테이블 정의 (-1로 방문 여부 체크)
distance = [-1 for _ in range(n + 1)]
distance[1] = 0 # 임의의 정점 x(1)
dfs(1, 0)

y = distance.index(max(distance))

# 거리 테이블 정의
distance = [-1 for _ in range(n + 1)]
distance[y] = 0 # x(1)에서 가장 먼 정점 y
dfs(y, 0)

print(max(distance))