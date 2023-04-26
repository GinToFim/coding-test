# 아이디어 : 맨 앞만, 맨 끝만 나누기
# 알고리즘 : dynamic programming
# 자료구조 : 

def solution(sticker):
    answer = 0
    n = len(sticker)
    
    if n == 1 :
        return sticker[0]
    
    if n == 2 :
        return max(sticker[0], sticker[1])
    
    sticker1 = sticker[:-1] # 맨 앞 포함
    sticker2 = sticker[1:] # 맨 뒤 포함
    
    dp1 = [0 for _ in range(n-1)]
    dp2 = [0 for _ in range(n-1)]
    
    dp1[0] = sticker1[0]
    dp1[1] = max(sticker1[0], sticker1[1])
    
    for i in range(2, n-1) :
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker1[i])
    
    dp2[0] = sticker2[0]
    dp2[1] = max(sticker2[0], sticker2[1])
    
    for i in range(2, n-1) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker2[i])

    return max(dp1[n-2], dp2[n-2])