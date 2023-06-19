# 알고리즘 : 투 포인터

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

start, end = 0, n - 1
result = abs(data[start] + data[end])
two_values = (data[start], data[end])

while start < end :
    hap = data[start] + data[end]
    
    if abs(hap) < result :
        result = abs(hap)
        two_values = (data[start], data[end])
        if result == 0 :
            break
            
    if hap < 0 :
        start += 1
    else :
        end -= 1
        
print(*two_values)