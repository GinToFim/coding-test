# arr는 queue, answer는 stack으로

from collections import deque

def solution(arr):
    answer = []
    queue = deque(arr)
    
    # 첫 번째는 요소는 그냥 추가
    answer.append(queue.popleft())
    
    # queue가 빌 때까지
    while queue :
        v = queue.popleft()
        # stack의 top과 다르다면 append
        if answer[-1] != v :
            answer.append(v)
        
    return answer