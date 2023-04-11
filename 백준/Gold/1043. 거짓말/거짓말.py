import sys
input = sys.stdin.readline

# find 연산 정의(경로 압축)
def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

# union 연산 정의
def union(a, b) :
    a = find(a)
    b = find(b) 
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

n, m = map(int, input().split())

# 진실을 아는 사람
truths = list(map(int, input().split()))
truths = truths[1:]

# 0번을 진실을 아는 사람으로 설정(why? 0이 제일 작음)
KNOW_TRUTH = 0
# 부모 테이블 정의
parent = [v for v in range(n + 1)]

for t in truths :
    parent[t] = KNOW_TRUTH
    
parties = []
for _ in range(m) :
    party_info = list(map(int, input().split()))
    
    p_cnt = party_info[0]
    party = party_info[1:]
    
    # 파티의 참석한 사람들에 대해 2명씩 union 연산 수행
    for i in range(p_cnt - 1) :
        union(party[i], party[i+1])
        
    parties.append(party_info)
    
result = 0

for party_info in parties :
    know = False
    
    p_cnt = party_info[0]
    party = party_info[1:]
    
    for i in range(p_cnt) :
        # 진실을 알고 있는 그룹에 속했을 경우
        if find(party[i]) == KNOW_TRUTH :
            know = True
            break
    
    if not know :
        result += 1

print(result)