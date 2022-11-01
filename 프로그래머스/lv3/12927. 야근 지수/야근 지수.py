# 아이디어 : 0. n이 works의 원소 합보다 크면 return 0
#           1. 최대 힙을 사용
#           2. n번만큼 힙의 원소를 1씩 줄이기
#              (최대 힙이라서 1씩 더함)

# 알고리즘 : 시간복잡도 n * log(len(works))
# 자료구조 : heap(heapq) 사용

import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-w for w in works]
    heapq.heapify(works)
    
    for _ in range(n) :
        w = heapq.heappop(works)
        heapq.heappush(works, w + 1)
    
    return sum([w ** 2 for w in works])