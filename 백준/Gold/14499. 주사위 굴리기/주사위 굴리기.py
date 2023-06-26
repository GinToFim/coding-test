# 아이디어 : 1. dx, dy - 동서북남(1, 2, 3, 4) 정의
#            2. 
# 알고리즘 : simulation
# 자료구조 : dictionary

import sys
input = sys.stdin.readline

# n, m(지도 크기), x, y(주사위 시작 위치), k(명령의 수)
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split())) # 명령들

# 주사위 정의 (한 칸 추가)
dice = [0 for _ in range(7)]

# 동서북남 정의(단, 인덱스를 위해 한 칸 추가)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 주사위 굴리기
def turn(direction) :
    # 방향 명시 (1, 2, 3, 4, 5, 6 ) - 전개도 기준
    #           위, 북, 동, 서, 남, 아래
    up, north, east, west, south, down = dice[1:]
    
    # 1(동쪽)  (1, 3, 6, 4) <- (4, 1, 3, 6) <- west, up, east,  
    if direction == 1 :
        dice[1], dice[3], dice[6], dice[4] = west, up, east, down
    # 2(서쪽) (1, 4, 6, 3) <- (3, 1, 4, 6) <- east, up, west, down
    elif direction == 2 :
        dice[1], dice[4], dice[6], dice[3] = east, up, west, down
    # 3(북쪽) (1, 2, 6, 5) <- (5, 1, 2, 6) <- south, up, north, down
    elif direction == 3:
        dice[1], dice[2], dice[6], dice[5] = south, up, north, down
    # 4(남쪽) (1, 5, 6, 2) <- (2, 1, 5, 6) <- north, up, south, down
    else :
        dice[1], dice[5], dice[6], dice[2] = north, up, south, down
        
        
for cmd in commands :
    nx = x + dx[cmd]
    ny = y + dy[cmd]
    
    # 범위 밖이라면 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue
    
    # 주사위 돌리기 실행
    turn(cmd)
    
    # 지도에 숫자가 0일 때
    if board[nx][ny] == 0 :
        board[nx][ny] = dice[6] # 바닥면 복사
    # 지도에 숫자가 있을 때
    else :
        dice[6] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny
    
    # 윗면 출력
    print(dice[1])