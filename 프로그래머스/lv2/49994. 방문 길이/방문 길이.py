# 아이디어 : 1. 그냥 그대로 기존 좌표계로 생각(2차원 리스트 X)
#           U(0, 1), D(0, -1), R(1, 0), L(-1, 0)
#           2. set에 ((기존 좌표), (이동 좌표)), ((이동 좌표), (기존 좌표)) 추가
#           3. 범위는 -5 ~ 5 사이
# 알고리즘 : implemenation
# 자료구조 : set

def solution(dirs):
    answer = 0
    move_types = {'U':(0, 1), 'D':(0, -1), 'R':(1, 0), 'L':(-1, 0)}
    
    # 원점
    x, y = 0, 0
    
    record_set = set()
    
    for di in dirs :
        dx, dy = move_types[di]
        
        nx = x + dx
        ny = y + dy
        
        # 범위 이내라면
        if -5 <= nx <= 5 and -5 <= ny <= 5 :
            # (기존 좌표), (이동 좌표) 추가
            record_set.add(((x, y), (nx, ny)))
            # (이동 좌표), (기존 좌표) 추가
            record_set.add(((nx, ny), (x, y)))
    
            # 좌표 갱신
            x, y = nx, ny
    
    return len(record_set) // 2