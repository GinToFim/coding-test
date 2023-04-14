# 아이디어 : union-find를 사용하여 중간 줄을 끊기
#          1. union-find 함수 설계 + parent 테이블
#          2. 특정 wires 리스트의 원소를 무시
#          3. parent 테이블을 Counter 클래스로 카운트

# 알고리즘 : union-find + 브루트 포스
#           wires 비교: O(n^2) = 10000
# 자료구조 : union-find, Counter 

from collections import Counter

def solution(n, wires):
    answer = []
    
    for i in range(n-1) :
        # parent 테이블 초기화
        parent = [x for x in range(n + 1)]
        for j in range(n-1) :
            # 끊을 노드에 해당하면 무시
            if i == j :
                continue
            a, b = wires[j]
            union_parent(parent, a, b) # union 연산 수행
        
        # 직접 find 연산을 위한 new_parent 테이블 생성
        new_parent = []
        for i in range(1, n + 1) :
            new_parent.append(find_parent(parent, i))
        
        # Counter를 이용하여 갯수세기
        counter = Counter(new_parent)
        counter = list(counter.values())
        answer.append(abs(counter[0] - counter[1]))
    
    return min(answer)

# find 연산 정의 (경로압축)
def find_parent(parent, x) :
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union 연산 정의
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b :
        parent[b] = a
    else :
        parent[a] = b


# 메모리: 10.3 MB, 시간: 12.78 ms