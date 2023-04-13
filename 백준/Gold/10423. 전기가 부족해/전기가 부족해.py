# 아이디어 : root 노드 추가하기
# 알고리즘 : mst, kruskal(parent, edges, sort, cycle) 
# 자료구조 : union-find

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

n, m, k = map(int, input().split())
power_plants = list(map(int, input().split()))

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

# 발전소에 있는 노드들 root 노드(0)으로 옮기기
for pp in power_plants :
    parent[pp] = 0

edges = []

for _ in range(m) :
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

# 간선 오름차순
edges.sort()

result = 0
for edge in edges :
    weight, u, v = edge
    
    # 사이클이 발생하지 않는다면
    if find(u) != find(v) :
        union(u, v)
        result += weight
    
print(result)