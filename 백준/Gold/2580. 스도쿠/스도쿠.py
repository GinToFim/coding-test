import sys
input = sys.stdin.readline

def row_check(r, num):
    if row_dict[r][num] != 0:
        return False
    return True

def col_check(c, num):
    if col_dict[c][num] != 0:
        return False
    return True

def square_check(r, c, num):
    if square_dict[r//3][c//3][num] != 0:
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
            row_dict[nr][num] = 1
            col_dict[nc][num] = 1
            square_dict[nr//3][nc//3][num] = 1
            dfs(depth + 1)
            square_dict[nr//3][nc//3][num] = 0
            col_dict[nc][num] = 0
            row_dict[nr][num] = 0
            board[nr][nc] = 0

board = [list(map(int, input().split()))
        for _ in range(9)]

# 0 인 위치 찾기
zeros = [(i, j) for i in range(9)
        for j in range(9) if board[i][j] == 0]


row_dict = [{x : 0 for x in range(1, 10)}
            for _ in range(9)]
col_dict = [{x : 0 for x in range(1, 10)}
            for _ in range(9)]
square_dict = [[{x : 0 for x in range(1, 10)} for _ in range(3)]
               for _ in range(3)]

for r in range(9):
    for c in range(9):
        if board[r][c] != 0:
            row_dict[r][board[r][c]] = 1
            col_dict[c][board[r][c]] = 1
            square_dict[r//3][c//3][board[r][c]] = 1

dfs(0)