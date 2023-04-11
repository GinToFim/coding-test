# 아이디어 : 1. 파티에 대한 정보를 모두 입력
#           2. 모든 파티에 대하여 union find 실행
#           3. 그 후에 다시 모든 파티원들에 대하여 진실이 아는 사람이 없으면 카운트
# 알고리즘 : union-find
# 자료구조 : disjoint-set

import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

truths = list(map(int, input().split()))
tcnt = truths[0]  # 진실을 아는 사람 수
truths = truths[1:] # 진실을 아는 사람들

# 부모 테이블 정의
parent = [v for v in range(n + 1)]

# 파티 수
parties = []
for _ in range(m) :
    parties.append(list(map(int, input().split())))
    
for party_info in parties :
    p_cnt = party_info[0]
    party = party_info[1:]
    
    for i in range(p_cnt - 1) :
        union_parent(parent, party[i], party[i+1])
        
# 진실을 아는사람들의 부모 찾기
truth_parent = [find_parent(parent, t) for t in truths]

result = 0

for party_info in parties :
    p_cnt = party_info[0]
    party = party_info[1:]
    
    # 현재 파티원들에 부모 찾기
    party_parent = [find_parent(parent, p) for p in party]    
    
    check = True
    # 만약에 진실을 아는사람들의 부모와 파티원들에 부모가 겹치면 무시
    for p in party_parent :
        if p in truth_parent :
            check = False
            break
    
    if check :
        result += 1
    
print(result)