import sys
input = sys.stdin.readline

def row_check(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    
    return True

def col_check(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False

    return True

def square_check(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False

    return True

def dfs(depth):
    # 종료 조건 정의
    if depth == len(zeros):
        for row in board:
            print(*row)
        exit() # 프로그램 종료

    nr, nc = zeros[depth]

    # 세 가지 조건에 만족한다면
    for num in range(1, 10):
        if row_check(nr, num) and col_check(nc, num) and square_check(nr, nc, num):
            board[nr][nc] = num
            dfs(depth + 1)
            board[nr][nc] = 0


board = [list(map(int, input().split()))
        for _ in range(9)]

# 0 인 위치 찾기
zeros = [(i, j) for i in range(9)
        for j in range(9) if board[i][j] == 0]

dfs(0)