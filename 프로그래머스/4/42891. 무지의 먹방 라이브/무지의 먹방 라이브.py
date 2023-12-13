# 아이디어: 0. k가 food_times의 합보다 크거나 같다면 -1
#          1. (시간, 인덱스 + 1)순으로 hq에 저장
#          2. 
# 알고리즘: 우선순위 큐, 
# 자료구조: heapq

import heapq

def solution(food_times, k):
    # k가 food_tiems의 합보다 크거나 같다면
    if sum(food_times) <= k :
        return -1
    
    hq = []
    
    # heapq에 (시간, 인덱스 + 1)순으로 저장
    for idx, time in enumerate(food_times):
        heapq.heappush(hq, (time, idx + 1)) 
    
    sum_value = 0 # 지금까지 총 걸린 시간
    prev = 0 # 이전 음식을 먹는데 걸리는 시간(단일)
    length = len(food_times) # 남은 음식의 수
    
    # 어느 음식을 다 먹을 때까지 가능하다면
    while sum_value + (hq[0][0] - prev) * length <= k:
        now = heapq.heappop(hq)[0]
        sum_value += (now - prev) * length # 총 시간 갱신
        length -= 1 # 남은 음식의 수 빼기
        prev = now # 이전 음식 갱신
        
    # 남은 음식 정렬
    result = sorted(hq, key = lambda x : x[1])
    
    return result[(k - sum_value) % length][1]