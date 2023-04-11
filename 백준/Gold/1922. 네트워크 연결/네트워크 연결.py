# 알고리즘 : MST, kruskal(parent, union, find, edges, sort, cycle)
# 자료구조 : union-find

import sys
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

n = int(input())
m = int(input())

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

# 간선 테이블 정의
edges = []

for _ in range(m) :
    a, b, c = map(int, input().split())
    edges.append((c, a, b)) # (비용, a, b) 순으로 저장
    
# 간선 오름차순 정렬
edges.sort()

result = 0 # 총 비용
cnt = 0 # 간선 개수

for edge in edges :
    cost, a, b = edge
    
    if cnt >= n - 1 :
        break
    
    # 사이클이 발생하지 않았다면
    if find(a) != find(b) :
        union(a, b)
        result += cost
        cnt += 1

print(result)