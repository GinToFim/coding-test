# 아이디어 : 1. 다리 길이 만큼의 bridge 리스트를 0으로 초기화
#           2. 다리의 트럭이 추가가 가능하다면 trucks 값 자체를 추가
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

result = 0
# 현재 다리 길이 만큼을 0으로 초기화
bridge = deque([0 for _ in range(w)])

# 마지막 트럭이 들어오고 그 트럭이 빠져나갈 때까지
while bridge:
    result += 1
    bridge.popleft() # 다리에서 하나 빼기
    
    # 지나갈 트럭이 있을 때
    if len(trucks) > 0:
        # 트럭을 추가해도 다리에 무게가 충분할 때 
        if sum(bridge) + trucks[0] <= L :
            bridge.append(trucks.popleft())
        else :
            # 트럭이 있지만 다리에 올리지 못할 경우 다리 공간 채우기
            bridge.append(0)
    
print(result)