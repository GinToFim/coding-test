# 아이디어 : 1. start, end는 움직이되, 나머지 하나는 완전탐색
#           
# 알고리즘 : brute force + two pointer
#           시간복잡도 = O(n^2) = 25,000,000

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬

min_value = 4 * int(1e9)

for i in range(n-2):
    start, end = i+1, n-1
    
    while start < end :
        hap = data[i] + data[start] + data[end]
        
        if abs(hap) < min_value:
            min_value = abs(hap)
            result = (data[i], data[start], data[end])
            
            if min_value == 0 :
                break
        
        # 음수라면 start 증가
        if hap < 0 :
            start += 1
        # 양수라면 end 감소
        else :
            end -= 1
            
print(*result)