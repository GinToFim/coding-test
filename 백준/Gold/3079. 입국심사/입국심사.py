# 아이디어 :
# 알고리즘 : binary search

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = []

for _ in range(n) :
    data.append(int(input()))
    
start, end = 0, max(data) * m
result = end

while start <= end :
    mid = (start + end) // 2
    
    total = 0 # 입국심사를 완료한 인원
    
    for x in data :
        total += mid // x
        
    if total >= m :
        result = min(result, mid)
        end = mid - 1
    else :
        start = mid + 1
        
print(result)