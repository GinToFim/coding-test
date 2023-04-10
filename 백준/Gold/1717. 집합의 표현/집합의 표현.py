# 아이디어
# 알고리즘 : union-find
# 자료구조 : disjoint set(union-find)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# find 연산 (경로 압축)
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [v for v in range(n + 1)]

for _ in range(m) :
    op, a, b = map(int, input().split())
    
    if op == 0 :
        union_parent(parent, a, b)
    else :
        if find_parent(parent, a) == find_parent(parent, b) :
            print('YES')
        else :
            print('NO')
