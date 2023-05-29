# 아이디어 : 
# 알고리즘 : 2D prefix sum

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]


def chess_board(color):
    # 누적합 2d 배열 선언 - color와 다를 것을 세는 누적합
    dp = [[0 for _ in range(m + 1)]
             for _ in range(n + 1)]
    
    for i in range(n):
        for j in range(m):
            # 짝수일 때는 color와 달라야 함
            if (i + j) % 2 == 0 :
                value = (board[i][j] != color)
            # 홀수일 때는 color와 같아야 함
            else :
                value = (board[i][j] == color)
            
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + value
    
    cnt = 1e9
    # k X k만큼 차지해야됨
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            tmp = dp[i+k-1][j+k-1] - dp[i+k-1][j-1] - dp[i-1][j+k-1] + dp[i-1][j-1]
            cnt = min(cnt, tmp)
    
    return cnt

result = min(chess_board('B'), chess_board('W'))
print(result)