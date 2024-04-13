# 아이디어: 
# 알고리즘: DP

def solution(triangle):
    n = len(triangle)
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    dp[1][0] = triangle[1][0] + dp[0][0]
    dp[1][1] = triangle[1][1] + dp[0][0]
    
    dp[2][0] = triangle[2][0] + dp[1][0]
    dp[2][1] = triangle[2][1] + max(dp[1][0], dp[1][1])
    dp[2][2] = triangle[2][2] + dp[1][1]
    
    for i in range(3, n):
        dp[i][0] = triangle[i][0] + dp[i-1][0]
        
        for j in range(1, i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

            
        dp[i][i] = triangle[i][i] + dp[i-1][i-1]
    
    return max(dp[n-1])