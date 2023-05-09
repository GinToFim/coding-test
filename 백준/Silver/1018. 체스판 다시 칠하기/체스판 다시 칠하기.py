import sys

input = sys.stdin.readline


# wb로 시작하는 것에 대하여 다시 칠하는 개수
def wb_cnt(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i + x][j + y] != wb[i][j]:
                cnt += 1
    return cnt


# bw로 시작하는 것에 대하여 다시 칠하는 개수
def bw_cnt(x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if board[i + x][j + y] != bw[i][j]:
                cnt += 1
    return cnt


n, m = map(int, input().split())

# 보드 입력받기
board = []
for _ in range(n):
    board.append(input().rstrip())

wb = [
    "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
    "WBWBWBWB", "BWBWBWBW"
]

bw = [
    "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
    "BWBWBWBW", "WBWBWBWB"
]

result = 1e7

for i in range(n - 7):
    for j in range(m - 7):
        tmp = min(wb_cnt(i, j), bw_cnt(i, j))
        result = min(result, tmp)

print(result)
