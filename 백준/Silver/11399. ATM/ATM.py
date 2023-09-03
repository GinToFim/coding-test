# 아이디어 : 걸리는 시간 오름차순 정렬
# 알고리즘 : 그리디, 정렬, 누적합

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

# 오름차순 정렬
data.sort()

prefix_sum = [0]
sum_value = 0

for x in data :
    sum_value += x
    prefix_sum.append(sum_value)
    
print(sum(prefix_sum))