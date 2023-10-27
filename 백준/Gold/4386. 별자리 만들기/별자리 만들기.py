# 아이디어: 1. parent, union, find, edges, sort, no-cycle
#           2. 좌표평면 (x1, y1), (x2, y2)에 대한 조합
# 알고리즘: 크루스칼, 조합

from itertools import combinations
import math
import sys
input = sys.stdin.readline

# find 함수 정의(경로 압축)
def find(x):
    # 루트 노드가 아니라면 찾을 때까지 탐색
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

# union 함수
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
n = int(input())
# 좌표평면 점 리스트
points = []

# 부모 테이블 정의
parent = [v for v in range(n)]

for i in range(n):
    x, y = map(float, input().split())
    points.append((x, y, i)) # (x좌표, y좌표, 해당 점의 인덱스)
    
# 가중치 리스트 정의
edges = []

for point_case in combinations(points, 2):
    (x1, y1, num1), (x2, y2, num2) = point_case
    
    cost = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    edges.append((cost, num1, num2))
    
# 가중치 리스트 오름차순 정렬
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    # 루트 노드가 다르다면 (사이클이 아니라면)
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)