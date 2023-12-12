import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    if sum(food_times) <= k:
        return -1
    
    hq = []
    
    for idx, time in enumerate(food_times):
        heapq.heappush(hq, (time, idx + 1))
        
    sum_value = 0 # 지금까지 먹기 위해 사용한 시간의 합
    prev = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수
    
    while sum_value + (hq[0][0] - prev) * length <= k:
        now = heapq.heappop(hq)[0]
        sum_value += (now - prev) * length
        length -= 1
        prev = now
        
    # 남은 음식 중에서 몇 번째 음식인지 확인
    result = sorted(hq, key=lambda x : x[1])
    # print(result)
    
    return result[(k - sum_value) % length][1]
    