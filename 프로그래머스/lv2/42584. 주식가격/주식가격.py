# 아이디어 : 1. prices를 queue로 변경
#           2. prices를 탐색하면서 
#               현재 가격보다 높거나 같으면 +1
#               현재 가격보다 낮으면 break하고 answer에 추가
# 알고리즘 : brute force
# 자료구조 : queue(deque)

from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices) # 큐 선언
    
    # 큐가 빌 때까지
    while prices :
        cnt = 0
        now = prices.popleft()
        
        for x in prices :
            cnt += 1
            if x < now :
                break
        
        answer.append(cnt)
                
        
    
    return answer