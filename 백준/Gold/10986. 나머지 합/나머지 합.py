# 아이디어
# 알고리즘

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

remain_info = [0 for _ in range(m)]
remain_info[0] += 1 # 누적합에서 0은 추가

sum_value = 0
for x in data :
    sum_value += x
    r = sum_value % m
    remain_info[r] += 1

result = 0
for r in remain_info :
    result += r * (r - 1) // 2

print(result)