# 아이디어: 1. 최소 투입하는 인원 구하기 -> dist 순열 경우의 수 구하기
#          2. 시계, 반시계 원형 판단은 weak 테이블 2배로 늘리기
#          3. 
# 알고리즘: 구현, 순열

from itertools import permutations

def solution(n, weak, dist):
    # weak의 길이
    weak_length = len(weak)
    
    # weak 테이블을 2배로 늘리기
    for i in range(weak_length):
        weak.append(weak[i] + n)
    
    # 최대 투입인원 수보다 더 많게 초기화(최솟값 탐색을 위해)
    answer = len(dist) + 1
    
    for friends in permutations(dist, len(dist)):
        for start in range(weak_length):
            count = 1 # 현재 투입되는 인원
            last_pos = weak[start] + friends[count-1] # 현재 인원이 커버 가능한 위치
            
            for idx in range(start+1, start + weak_length):
                # 다음 위치를 커버하지 못한다면
                if weak[idx] > last_pos:
                    count += 1 # 인원 늘리기
                    
                    # 투입된 인원이 가능한 인원보다 많다면
                    if count > len(dist):
                        break
                    
                    # 다음 위치부터 커버 가능한 위치까지를 구하기
                    last_pos = weak[idx] + friends[count-1]
            
            # 최솟값 갱신하기
            answer = min(answer, count)
    
    # 만약 전부 투입해도 불가능하다면
    if answer > len(dist):
        return -1
    
    return answer