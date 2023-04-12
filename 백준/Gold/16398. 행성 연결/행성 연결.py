# 알고리즘 : MST, kruskal(parent, union, find, edge, sort, cycle)
# 자료구조 : union - find

import sys
input = sys.stdin.readline

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b) 
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

# 간선 테이블
edges = []

for a in range(1, n + 1) :
    row = list(map(int, input().split()))
    
    for b in range(a + 1, n + 1) :
        edges.append((row[b-1], a, b))

# 간선 테이블 정렬
edges.sort()

result = 0
cnt = 0

for edge in edges :
    cost, a, b = edge
    
    if cnt == n - 1 :
        break
    
    # 사이클 발생 X
    if find(a) != find(b) :
        union(a, b)
        result += cost
        cnt += 1
        
print(result)