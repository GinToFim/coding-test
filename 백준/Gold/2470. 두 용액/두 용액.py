# 아이디어 : 1. 오름차순 정렬
#           2. 두 용액의 절댓값 합이 음수일 때 start를 증가시키면 합 증가
#              두 용액의 절댓값 합이 양수일 때 end를 감소시키면 합 감소
#           3. 0이면 바로 종료
# 알고리즘 : sort, two pointer

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

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