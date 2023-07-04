# 아이디어 : 1. 두 리스트를 큐(덱)로 변경
#           2. 
# 알고리즘 : 
# 자료구조 : queue(deque)

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 1 # 현재 날짜
    cnt = 0 # 배포 기능 개수
    
    while progresses :
        # 배포가 가능하다면
        while len(progresses) > 0 : 
            if progresses[0] + day * speeds[0] >= 100 :
                progresses.popleft()
                speeds.popleft()
                cnt += 1
            else :
                break
        
        # 배포할 기능이 있다면
        if cnt > 0 :
            answer.append(cnt)
            cnt = 0
        day += 1
    
    return answer