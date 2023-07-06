# 아이디어 : 1. second, bridge : 큐 사용
#            2. bridge의 합과 truck_weights[0] 이 제한 무게보다 작으면
#            3. second와 bridge 원소 추가
# 자료구조 : queue(deque)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 시간
    
    truck_weights = deque(truck_weights) # 다리를 건널 트럭들
    bridge_second = deque() # 다리를 건너고 있는 시간들
    bridge_weights = deque() # 다리 위에 무게
    
    # 맨 앞 트럭 한 대 추가하기
    bridge_second.append(0)
    bridge_weights.append(truck_weights.popleft())
    
    # 다리가 빌 때까지
    while bridge_weights :
        answer += 1
        
        # 1초씩 추가
        bridge_second = deque(sec + 1 for sec in bridge_second)
        
        # 트럭이 도착했다면
        if bridge_second[0] >= bridge_length :
            bridge_second.popleft()
            bridge_weights.popleft()
        
        # 남아있는 트럭이 있으면
        if len(truck_weights) > 0 :
            # 그리고 아직 다리의 무게가 여유가 있으면
            if sum(bridge_weights) + truck_weights[0] <= weight :
                bridge_second.append(0)
                bridge_weights.append(truck_weights.popleft())
    
    # 끝나는 시간 1초 추가하기
    answer += 1
    
    return answer