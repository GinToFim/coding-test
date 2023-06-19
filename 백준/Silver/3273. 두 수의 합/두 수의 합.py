# 아이디어 : 1. 오름차순 정렬
#           2. start를 증가시키면 두 수의 합 무조건 증가
#              end를 감소시키면 두 수의 합 무조건 감소
# 알고리즘 : sort, two pointer

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

# 오름차순 정렬
data.sort()

start, end = 0, n - 1
result = 0

while start < end :
    hap = data[start] + data[end]
    
    if hap == x :
        result += 1
        start += 1
    elif hap < x :
        start += 1
    else :
        end -= 1

print(result)