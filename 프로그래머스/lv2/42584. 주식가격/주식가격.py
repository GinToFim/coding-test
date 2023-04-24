# 아이디어 : 
# 알고리즘 :
# 자료구조 : 

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        now = prices.popleft()
        cnt = 0
        
        for price in prices:
            if now > price :
                # 1초간 본인도 포함
                cnt += 1
                break
            cnt += 1
            
        answer.append(cnt)

    return answer