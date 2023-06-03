# 아이디어
# 알고리즘 : 구현

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 돌리는 횟수
for _ in range(r):
    # 돌려야하는 직사각형 개수
    rect_cnt = min(n, m) // 2

    for i in range(rect_cnt):
        # 첫 시작점
        x, y = i, i
        value = graph[x][y]

        # 좌 (위 -> 아래) (이동하는 위치)
        # 0, 1, 2 -> 1, 2, 3
        for d in range(i + 1, n - i):
            x = d
            prev_value = graph[x][y]
            graph[x][y] = value
            value = prev_value

        # 하 (왼쪽->오른쪽)
        # 0, 1, 2 -> 1, 2, 3
        for d in range(i + 1, m - i):
            y = d
            prev_value = graph[x][y]
            graph[x][y] = value
            value = prev_value

        # 우 (아래 -> 위)
        # 3, 2, 1 -> 2, 1, 0
        for d in range(i + 1, n - i):
            x = n - d - 1
            prev_value = graph[x][y]
            graph[x][y] = value
            value = prev_value

        # 상 (오른쪽 -> 왼쪽)
        # 3, 2, 1 -> 2, 1, 0
        for d in range(i + 1, m - i):
            y = m - d - 1
            prev_value = graph[x][y]
            graph[x][y] = value
            value = prev_value
        
for row in graph:
    print(*row)