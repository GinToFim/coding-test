# second, bridge : 큐 사용
# bridge의 합과 truck_weights[0] 이 제한 무게보다 작으면
# second와 bridge 원소 추가

from collections import deque

def solution(bridge_length, weight, truck_weights):
    result = 0 # 걸리는 시간
    bridge = deque() # 다리 위 트럭들 queue
    second = deque() # 초를 재는 queue
    
    bridge.append(truck_weights.pop(0))
    second.append(0)
    
    # bridge 가 빌 때까지
    while bridge :
        result += 1
        
        for i in range(len(second)) :
            second[i] += 1
            
        if second[0] == bridge_length : 
            bridge.popleft()
            second.popleft()

        if len(truck_weights) > 0 :
            if sum(bridge) + truck_weights[0] <= weight :
                truck = truck_weights.pop(0)
                bridge.append(truck)
                second.append(0)
                
    result += 1
    return result