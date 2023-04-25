# 아이디어 : 1. (소요시간, 요청시점)을 기준으로 heap 수행
#           2. 
# 알고리즘 : heap 
# 자료구조 : heapq

import heapq

def solution(jobs):
    answer = 0
    # 작업 요청이 가능한 시간(start), 현재 시간(now)
    start, now = -1, 0
    cnt = 0 # 작업이 처리된 개수
    hq = []
    
    while cnt < len(jobs) :
        for job in jobs :
            # 작업 실행이 가능하다면
            if start < job[0] <= now :
                heapq.heappush(hq, (job[1], job[0])) # 소요시간, 요청시간순으로
        
        # 만약 hq에 원소가 있다면
        if hq :
            njob = heapq.heappop(hq)
            start = now # 요청 가능한 시간을 현재 시간으로 변경
            now += njob[0] # 소요시간 추가 
            answer += now - njob[1] # 총 시간에는 (현재시간 - 요청시간) 추가
            cnt += 1
        else :
            now += 1 # 현재시간 추가
    
    return answer // cnt