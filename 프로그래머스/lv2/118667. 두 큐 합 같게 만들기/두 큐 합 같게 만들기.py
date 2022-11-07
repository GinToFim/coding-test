# 아이디어 : sum이 큰 쪽에서 작은 쪽으로 이동
# 알고리즘
# 자료구조 : queue(deque)

from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    limit = len(queue1) * 2 + len(queue2) * 2
    
    # 두 수의 합이 짝수이면 
    if (sum1 + sum2) % 2 == 1 :
        return -1

    while sum1 != sum2 :
        if sum1 > sum2 :
            v = queue1.popleft()
            queue2.append(v)
            sum1 -= v
            sum2 += v
        else :
            v = queue2.popleft()
            queue1.append(v)
            sum2 -= v
            sum1 += v
        
        answer += 1
        
        if answer == limit :
            answer = -1
            break
    
    return answer