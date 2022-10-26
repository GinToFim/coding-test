import heapq

def solution(scoville, K):
    answer = 0
    
    # list를 heapq로 변경
    heapq.heapify(scoville) 
    
    while scoville :
        first = heapq.heappop(scoville)

        # 만약에 첫 번째 원소가 K보다 크다면 return
        if first >= K :
            return answer
        if len(scoville) <= 0 :
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        answer += 1
    

    return answer