# 아이디어 
# (location은 0, 1, 2, 3)
# location : 0 1 2 3
# 대기목록  : A B C D
# 우선순위  : 2 1 3 2

# -> C D A B (2의 위치인 C가 먼저 제일 먼저 출력)

from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    
    # 우선순위와 위치 큐(deque)로 변경
    priorities = deque(priorities)
    positions = deque(x for x in range(n))
    num = 1 # 순서
    
    # priorities(큐)가 빌 때까지
    while priorities : 
        # 제일 큰 중요도
        max_val = max(priorities)
        
        prior = priorities.popleft()
        pos = positions.popleft()
        
        # 제일 큰 중요도 와 현재 중요도가 일치 할 때 
        if max_val == prior :
            # 위치가 맞다면
            if pos == location :
                return num
            else :
                num += 1 # 다르면 순번 추가
        else :
            priorities.append(prior)
            positions.append(pos)
    
    return num