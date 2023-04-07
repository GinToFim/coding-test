# 아이디어 : 인출해야 할 최소 금액은 몇인가?
#          -> 이 정도 금액이면 충분히 적은가?
# 알고리즘 : 이진 탐색, 파라메트릭

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []
for _ in range(n) :
    data.append(int(input()))
    
start, end = max(data), sum(data)
result = sum(data)

while start <= end :
    mid = (start + end) // 2
    
    money = mid # 인출한 금액
    cnt = 1 # 인출한 횟수
    
    for i in range(n) :
        if money - data[i] < 0 :
            money = mid - data[i]
            cnt += 1
        else :
            money -= data[i]
    
    # 인출한 횟수가 충분히 적다면(돈 줄이기)
    if cnt <= m :
        result = min(result, mid)
        end = mid - 1
    # 인출한 횟수가 너무 많다면(돈 늘리기)
    else :
        start = mid + 1

print(result)