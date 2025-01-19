import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip()))
        for _ in range(9)]

# 0의 위치를 담는 리스트
zeros = [(x, y) for x in range(9)
           for y in range(9) if board[x][y] == 0]

# 같은 행에 해당 숫자가 있는지 체크
def row_check(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    
    return True

# 같은 열에 해당 숫자가 있는지 체크
def col_check(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    
    return True

# 같은 정사각형에 해당 숫자가 체크
def square_check(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False
    
    return True

# 백트래킹 함수 정의
def dfs(depth):
    # 종료조건
    if depth == len(zeros):
        for row in range(9):
            print(''.join(map(str, board[row])))
        exit() # 프로그램 종료
    
    # 현재 확인할 위치
    nr, nc = zeros[depth]
                
    for num in range(1, 10):
        # 세 가지 조건에 만족하면 백트래킹 수행
        if row_check(nr, num) and col_check(nc, num) and square_check(nr, nc, num):
            board[nr][nc] = num
            dfs(depth + 1)
            board[nr][nc] = 0


dfs(0)