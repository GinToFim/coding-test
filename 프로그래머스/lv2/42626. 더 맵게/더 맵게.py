# 아이디어 : 가장 낮은 2개의 수를 뽑기, 하지만 min을 사용하면 시간복잡도 X
# 자료구조 : heap(heapq) 사용

import heapq

def solution(scoville, K):
    answer = 0
    
    # heap으로 변환
    heapq.heapify(scoville)
    
    while True :
        first = heapq.heappop(scoville)
        
        if first >= K :
            return answer
        
        if len(scoville) <= 0 :
            break
        
        second = heapq.heappop(scoville)
        val = first + second * 2
        heapq.heappush(scoville, val)
        answer += 1
    
    return -1