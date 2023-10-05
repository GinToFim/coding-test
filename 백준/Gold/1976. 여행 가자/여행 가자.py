# 아이디어
# 알고리즘 : union-find
# 자료구조 : disjoint set

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# find 연산 (경로압축)
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

n = int(input())
m = int(input())

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

for i in range(1, n + 1) :
    connects = list(map(int, input().split()))
    
    for j in range(1, n + 1) :
        # 도시가 연결되어 있다면
        if connects[j-1] == 1 :
            union_parent(parent, i, j)

# 여행 계획
plans = list(map(int, input().split()))            

result = set([find_parent(parent, plan) for plan in plans])

if len(result) <= 1 :
    print("YES")
else :
    print("NO")