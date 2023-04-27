# 아이디어 : 1. 첫 번째 아파트에서 첫 번째 기지국 사이에 전파가 닿지 않는 거리
#               마지막 아파트에서 마지막 기지국 사이에 전파가 닿지 않는 거리 추가
#           2. 각각 설치된 기지국 사이에 전파가 닿지 않는 거리 추가
#           3. 만약 각 거리가 음수이면 무시
#           4. 
# 알고리즘 : N = 2* 10 ** 9 -> 이진 탐색
# 자료구조 : 

import math

def solution(n, stations, w):
    answer = 0
    distances = []
    
    # 1 아파트와 1 station 사이의 No 전파 거리 추가
    distances.append(stations[0]-w-1)
    # n 아파트와 m station 사이의 No 전파 거리 추가
    distances.append(n - (stations[-1] + w))
    
    # 설치된 기지국 사이에 전파가 닿지 않는 거리를 추가
    for i in range(1, len(stations)) :
        dist = (stations[i]-w-1) - (stations[i-1]+w)
        distances.append(dist)
        
    # 사이 거리마다 기지국 개수 추가
    for dist in distances :
        if dist <= 0 :
            continue
        
        # 올림
        answer += math.ceil(dist / (2 * w + 1))
    
    
    return answer