# 아이디어 : 1. dp 테이블 무한대로 초기화
#           2. (x + n, 2 * x, 3 * x) min 값 구하기
# 알고리즘 : Dynamic Programming

def solution(x, y, n):
    INF = 10 ** 7
    dp = [INF for _ in range(y + 1)]
    dp[x] = 0
    
    for i in range(x, y + 1) :
        if dp[i] == INF :
            continue
            
        for next_i in (i + n, 2 * i, 3 * i) :
            if next_i <= y :
                dp[next_i] = min(dp[next_i], dp[i] + 1)
    
    if dp[y] == INF :
        return -1
    else :
        return dp[y]
