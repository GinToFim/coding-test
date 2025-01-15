n, m, x, y, k = map(int, input().split())

graph = [list(map(int, input().split()))
        for _ in range(n)]

commands = list(map(int, input().split()))

# 주사위 정의 
dice = [0] * 7

# 동서북남 정의 (인덱스를 위해 한 칸 추가)
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# 주사위 굴리기
def roll(direction):

    # 방향 (1, 2, 3, 4, 5, 6)
    #       위 북 동 서 남 아래

    # 1(동쪽) 1, 3, 6, 4 <- 4, 1, 3, 6
    if direction == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    # 2(서쪽) 1, 4, 6, 3 <- 3, 1, 4, 6
    elif direction == 2:
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    # 3(북쪽) 1, 2, 6, 5 <- 5, 1, 2, 6
    elif direction == 3:
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
    # 4(남쪽) 1, 5, 6, 2 <- 2, 1, 5, 6
    else:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]

for cmd in commands:
    nx = x + dx[cmd]
    ny = y + dy[cmd]

    # 범위 밖이라면 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m :
        continue

    # 주사위 돌리기 실행
    roll(cmd)

    # 지도에 숫자가 0일 때
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[6] # 주사위에 바닥면 복사
    else:
        dice[6] = graph[nx][ny]
        graph[nx][ny] = 0

    # 위치 변경
    x, y = nx, ny

    # 위쪽 주사위 출력
    print(dice[1])