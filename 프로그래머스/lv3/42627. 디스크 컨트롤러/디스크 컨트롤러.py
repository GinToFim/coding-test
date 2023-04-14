# 아이디어 : 
# 알고리즘 : heap
# 자료구조 : heapq(heap)

import heapq

def solution(jobs):
    # 작업 요청이 가능한 시간(start), 현재 시간(now)
    start, now = -1, 0
    cnt = 0 # 작업을 처리한 개수 
    result = 0 # 총 시간
    hq = [] # 힙큐
    
    while cnt < len(jobs) :
        for job in jobs : # job[0] : 시점, job[1] : 걸리는 시간
            # 작업이 요청이 가능한 시간(start)과 현재 시간(now) 사이이면
            if start < job[0] <= now :
                heapq.heappush(hq, (job[1], job[0]))
                
        # 만약 heap에 원소가 있다면
        if hq : 
            njob = heapq.heappop(hq) # [걸리는 시간, 시점]
            start = now # 작업 요청 가능한 시간을 현재 시간으로 옮김
            now += njob[0] # 현재시간은 걸리는 시간 추가
            result += now - njob[1] # 총 시간에는 현재시간 - 작업이 들어온 시점
            cnt += 1 # 작업 개수 추가
        # heap이 비워져있다면
        else  :
            now += 1 # 현재 시간 추가
        
    return result // len(jobs)