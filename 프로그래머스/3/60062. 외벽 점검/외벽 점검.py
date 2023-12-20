# 아이디어: 1. 원형 형태를 2배로 하여 일자 형태로 바꾸기
#          2. dist 테이블에 대한 경우의 수를 순열로 따지기
#          3. 0 ~ (dist 길이 - 1)을 시작점으로 설정
#          4. 
# 알고리즘: 완전 탐색, 순열

from itertools import permutations

def solution(n, weak, dist):
    # 취약 지점의 길이를 2배로 늘려서 '일자' 형태로 변경
    weak_length = len(weak)
    
    for i in range(weak_length):
        weak.append(weak[i] + n)
    
    # 투입할 최대 친구 수보다 많게 초기화(최소값을 찾아야 되므로)
    answer = len(dist) + 1
    
    # 커버 가능한 친구들에 거리를 순열
    for friends in permutations(dist, len(dist)): 
        # 0 ~ (length + 1)까지의 위치를 각각 시작점으로 설정
        for start in range(weak_length):
            count = 1 # 투입할 친구의 수
            
            # 처음 친구가 커버 가능한 마지막 위치
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 마지막까지 모든 취약 지점 확인
            for idx in range(start, start + weak_length):
                # 현재 친구가 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[idx]:
                    count += 1 # 새로운 친구 투입
                    
                    # 새로운 친구를 더 투입할 수 없다면
                    if count > len(dist):
                        break
                    
                    # 다음 위치부터 커버 가능한 위치
                    position = weak[idx] + friends[count - 1]
                    
            answer = min(answer, count)
    
    # 취약 지점을 점검할 수 없다면
    if answer > len(dist):
        return -1
    
    return answer