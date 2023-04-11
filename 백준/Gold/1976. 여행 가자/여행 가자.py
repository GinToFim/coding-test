# 알고리즘 : union-find
# 자료구조 : disjoint-set

import sys
input = sys.stdin.readline

# find 연산 정의(경로 압축)
def find(parent, x) :
    if parent[x] != x :
        parent[x] = find(parent, parent[x])
    return parent[x]

# union 연산 정의
def union(parent, a, b) :
    a = find(parent, a)
    b = find(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
        
n = int(input())
m = int(input())

# 부모 테이블 초기화
parent = [v for v in range(n + 1)]

for i in range(1, n + 1) :
    row = list(map(int, input().split()))
    
    for j in range(1, n + 1) :
        if row[j-1] == 1 :
            union(parent, i, j)

# 여행 계획 입력
plans = list(map(int, input().split()))

result = [find(parent, plan) for plan in plans]
if len(set(result)) <= 1 :
    print("YES")
else :
    print("NO")