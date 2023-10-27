# 아이디어: 1. parent, union, find 정의
#           2. 가중치(edges) 오름차순 정렬 + no cycle
# 알고리즘: 최소 신장 트리, 크루스칼

import sys
input = sys.stdin.readline

# find 함수 정의
def find(x):
    # 루트 함수가 아니라면
    if parent[x] != x :
        parent[x] = find(parent[x])
    
    return parent[x]

# union 함수 정의
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
    
n, m = map(int, input().split())
# parent 테이블 정의
parent = [v for v in range(n + 1)]

# 가중치 리스트 정의 및 입력
edges = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 정렬을 위해 cost 먼저

# 가중치 리스트 오름차순 정렬
edges.sort()

result = 0

for edge in edges:
    cost, a, b = edge
    
    # 사이클 탐색
    if find(a) != find(b):
        union(a, b)
        result += cost
        
print(result)