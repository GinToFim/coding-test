# 아이디어 : 
# 알고리즘 : 브루트 포스

import sys
input = sys.stdin.readline

BW = "BW" * 8
BW_board = []
for i in range(8):
    BW_board.append(BW[i:i + 8])

WB = "WB" * 8
WB_board = []
for i in range(8):
    WB_board.append(WB[i:i + 8])

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
    
def color_cnt(color_board, x, y):
    cnt = 0
    
    for i in range(8):
        for j in range(8):
            if board[i+x][j+y] != color_board[i][j]:
                cnt += 1
    
    return cnt


result = 1e9
for i in range(n - 7):
    for j in range(m - 7):
        tmp = min(color_cnt(BW_board, i, j), color_cnt(WB_board, i, j))
        result = min(result, tmp)
        
print(result)