# 아이디어 : 1. 우선순위(priorities)와 프로세스(processes) 큐 선언
#           2. 
# 자료구조 : queue(deque)

from collections import deque

def solution(priorities, location):
    rank = 1
    processes = deque(x for x in range(len(priorities)))
    priorities = deque(priorities)
    
    # 큐가 빌 때까지
    while processes :
        # 맨앞이 가장 우선순위가 높다면
        if priorities[0] == max(priorities):
            priorities.popleft()
            now = processes.popleft()
            if now == location :
                return rank
            else :
                rank += 1
        # 맨앞이 가장 우선순위가 높지 않다면
        else:
            priorities.append(priorities.popleft())
            processes.append(processes.popleft())
