# 아이디어 : 1. p[0] + s[0] * days >= 100 이면 pop하기
#           2. pop에 대한 개수만큼 완성인 상태 늘리기
# 알고리즘 : 
# 자료구조 : queue(deque)

from collections import deque

def solution(progresses, speeds):
    answer = []
    days = 1 # 날짜
    cnt = 0 # 배포 개수
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    # progresses가 빌 때까지
    while progresses :
        if progresses[0] + speeds[0] * days >= 100 :
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else :
            if cnt > 0 :
                answer.append(cnt)
                cnt = 0
            days += 1
    
    # 남은 배포 append
    answer.append(cnt)
    
    return answer