# 아이디어
# 알고리즘 : Dynamic Programming

def solution(triangle):
    n = len(triangle)
    triangle[1][0] += triangle[0][0]
    triangle[1][1] += triangle[0][0]
    
    for i in range(2, n) :
        # 맨 앞 (0)
        triangle[i][0] += triangle[i-1][0]
        
        # 1 ~ i - 1 까지
        for j in range(1, i) :
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
        
        # 맨 뒤 (i)
        triangle[i][i] += triangle[i-1][i-1]

    return max(triangle[n-1])