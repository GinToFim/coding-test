# 아이디어 : 1. union, find 함수 정의 
#           2. 고리처럼 연결되어 있는 card 번호 찾기
# 알고리즘 : 
# 자료구조 : union-find

from collections import Counter

def solution(cards):
    answer = 0
    cards = [0] + cards # 인덱스를 맞추기 위해서 추가
    parent = [x for x in range(len(cards))]
    visited = [False] * len(cards)
    
    # parent의 원소가 0이라면 아직 visited X
    for i in range(1, len(cards)) :
        tmp = []
        # 이미 방문한적이 있으면 무시
        if visited[i] :
            continue
            
        x = cards[i]
        while x not in tmp :
            if not visited[x] :
                tmp.append(x)
                x = cards[x]

        tmp.sort()
        for x in tmp :
            visited[x] = True

        if len(tmp) >= 2 :
            for i in range(len(tmp)-1) :
                union_parent(parent, tmp[i], tmp[i+1])
    
    counter = Counter(parent[1:])

    counter = sorted(counter.values(), reverse=True)
    if len(counter) <= 1 :
        return 0

    return counter[0] * counter[1]

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