# 아이디어 : 오름차순으로 정렬하고 맨 처음에 start, 맨 끝에 end 
# 알고리즘 : sort, two pointer

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

start, end = 0, n - 1
result = 0

while start < end :
    hap = data[start] + data[end]
    
    if hap == m :
        result += 1
        start += 1
    elif hap > m :
        end -= 1
    else :
        start += 1
        
print(result)