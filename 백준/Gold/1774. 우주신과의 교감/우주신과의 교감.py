# 아이디어 : 1. 이미 연결되어 있는 점들과 안되어 있는 점들 나누기
#           2. 연결이 안되어 있는 점들만 거리를 구하기 (그중 최소만 신장트리에 추가)
# 알고리즘 : MST, Kruskal(parent, union, find, edges, sort, cycle)
# 자료구조 : union-find

import math
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# find 연산 (경로 압축)
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

# union 연산
def union(a, b) :
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

points = [(0, 0)]
for i in range(1, n + 1) :
    x, y = map(int, input().split())
    points.append((x, y))

cnt = 0 # 현재 연결된 간선 개수

# 이미 연결되어 있는 점 union 연산
for _ in range(m) :
    a, b = map(int, input().split())
    union(a, b)
    cnt += 1

# 간선 테이블
edges = []
# 모든 간선 추가
for v in range(1, n + 1) :
    x, y = points[v]
    
    for i in range(v + 1, n + 1) :
        tx, ty = points[i]
        cost = math.sqrt((x - tx)**2 + (y - ty)**2)
        
        edges.append((cost, v, i))

# 간선 오름차순 정렬
edges.sort()
result = 0
for edge in edges :
    cost, a, b = edge
    
    # 사이클이 발생하지 않으면
    if find(a) != find(b) :
        union(a, b)
        result += cost
        
print(f"{result:0.2f}")