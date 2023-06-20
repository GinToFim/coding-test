# 아이디어 : 1. 사과 정보 및 뱡향 변환 정보 입력
#           2. 방향 변환 함수 정의
#           3. 뱀에 대한 정보를 queue에 담음
# 알고리즘 : simulation
# 자료구조 : deque(queue)

from collections import deque
import sys
input = sys.stdin.readline

# 보드의 크기 입력
n = int(input())
board = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 사과의 개수 입력 (사과가 있는 곳은 1로 표시)
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

# 방향 변환 정보
dir_dict = dict()
l = int(input())
for _ in range(l) :
    x, c = input().split()
    dir_dict[int(x)] = c
    
# 뱀은 처음에 오른쪽(동쪽) (동, 남, 서, 북) 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 회전 함수 정의
def turn(direction, c):
    # 왼쪽 회전이라면
    if c == 'L' :
        direction = (direction - 1) % 4
    # 오른쪽 회전이라면
    else :
        direction = (direction + 1) % 4
    
    return direction

# 시물레이션 함수 정의
def simulation() :
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 있는 곳은 2로 표시
    direction = 0 # 처음은 동쪽
    result = 0 # 결과
    
    # 큐 및 시작노드 선언
    queue = deque()
    queue.append((x, y))
    
    while True :
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 보드 범위 내(1~n)에 있고, 뱀이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2 :
            # 사과가 없다면(0)
            if board[nx][ny] == 0 :
                board[nx][ny] = 2 # 머리 이동
                queue.append((nx, ny))
                # 이동하고 꼬리제거
                px, py = queue.popleft()
                board[px][py] = 0
            # 사과가 있다면(1)
            if board[nx][ny] == 1 :
                # 머리만 이동 (꼬리 고정)
                board[nx][ny] = 2
                queue.append((nx, ny))
        # 벽이나 뱀에 부딪쳤다면
        else :
            result += 1
            return result
        
        x, y = nx, ny # 다음 위치로 머리 이동
        result += 1
        
        # 현재 시간이 뱡향을 회전할 시간이라면
        if result in dir_dict :
            direction = turn(direction, dir_dict[result])
            
print(simulation())