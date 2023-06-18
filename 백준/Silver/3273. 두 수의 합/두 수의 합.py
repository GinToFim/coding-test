# 아이디어 : 1. 리스트 오름차순 정렬하기
#           2. start, end를 0, n - 1로 설정
#           3. 합이 x보다 작다면 start += 1
#              합이 x보다 크거나 같다면 end -= 1
# 알고리즘 : 투 포인터

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
x = int(input())

data.sort() # 오름차순 정렬

start, end = 0, n - 1
result = 0

while start < end :
    hap = data[start] + data[end]
    
    if hap == x :
        result += 1
        end -= 1
    elif hap < x :
        start += 1
    else :
        end -= 1

print(result)