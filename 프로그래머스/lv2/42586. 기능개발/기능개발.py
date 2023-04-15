# day를 사용하기
# 자료구조 : queue(deque)

from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0 # 배포할 개수
    day = 0 # 지나는 날짜
    
    # 큐가 빌 때까지
    while progresses :
        # 이번 날짜에 배포가 가능하다면
        if (progresses[0] + day * speeds[0]) >= 100 :
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        else :
            # 배포할 개수가 있다면
            if cnt >= 1 :
                answer.append(cnt)
                cnt = 0
            # 배포할 것도 없고 지금 날짜에는 아무것도 안되면
            else :
                day += 1
    
    # 마지막 배포할 개수 추가
    answer.append(cnt)
    
    return answer