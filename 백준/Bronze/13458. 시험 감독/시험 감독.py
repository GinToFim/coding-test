# 아이디어
# 알고리즘

import math
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())

# 감독관(b)만큼 data의 요소들 빼기
data = [x - b for x in data]
result = n # 최소 감독관 수

for x in data :
    if x > 0 :
        result += math.ceil(x / c)

print(result)