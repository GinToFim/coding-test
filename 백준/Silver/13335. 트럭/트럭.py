# 아이디어 : 1. 다리(bridge)를 다리의 길이(w) 만큼 0으로 초기화
#           2. 
# 자료구조 : deque(queue)

from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

# 다리를 다리의 길이(w) 만큼 초기화 
bridge = deque(0 for _ in range(w))

result = 0

# 다리가 다 빌 때까지
while bridge :
    bridge.popleft() # 다리 요소 하나 빼기
    
    # 지나갈 트럭이 있을 때
    if len(trucks) > 0:
        # 트럭이 다리를 지나가도 무게가 충분할 때
        if sum(bridge) + trucks[0] <= L:
            bridge.append(trucks.popleft())
        # 빈 거(0) 추가
        else :
            bridge.append(0)
            
    result += 1
    
    
print(result)