# 알고리즘 : MST, Kruskal(parent, union, find, edge, sort, cycle)
# 자료구조 : union-find

import sys
input = sys.stdin.readline

# find 연산 정의(경로 압축)
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

while True :
    m, n = map(int, input().split())
    
    if m == 0 and n == 0 :
        break

    # 부모 테이블 초기화
    parent = [v for v in range(m)]

    # 간선 테이블
    edges = []

    result = 0 # 총 비용
    cnt = 0 # 최소 신장 트리에서 간선 개수

    for _ in range(n) :
        a, b, c = map(int, input().split())
        edges.append((c, a, b)) # (비용, a, b)순으로 저장
        result += c

    # 간선 오름차순 정렬
    edges.sort()

    for edge in edges :
        cost, a, b = edge

        # 최소 신장 트리가 완성되었다면
        if cnt == m - 1 :
            break

        # 사이클이 발생하지 않는다면
        if find(a) != find(b) :
            union(a, b)
            result -= cost
            cnt += 1

    print(result)