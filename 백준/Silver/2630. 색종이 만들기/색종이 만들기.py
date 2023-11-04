# 아이디어: 1. 현재 위치와 다음 위치와 색깔이 다르다면 종이를 4칸으로 쪼개기
# 알고리즘: 분할정복

import sys
input = sys.stdin.readline

def cut(x, y, n):
    # 현재 위치 색깔 기억
    color = board[x][y]
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색깔이 다르다면
            if color != board[i][j]:
                # 종이를 4구역으로 쪼개기
                cut(x, y, n // 2)
                cut(x, y + n // 2, n // 2)
                cut(x + n // 2, y, n // 2)
                cut(x + n // 2, y + n // 2, n // 2)
                return
    
    if color == 0:
        result.append(0)
    else:
        result.append(1)
        

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = [] # 색깔 기억

cut(0, 0, n)

print(result.count(0))
print(result.count(1))