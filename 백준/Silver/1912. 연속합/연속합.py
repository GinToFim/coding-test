# 아이디어 : 1. 양수라면 무조건 더하기
#            2. 음수라면 현재값으로 기억
# 알고리즘 : dp

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
    data[i] = max(data[i], data[i] + data[i-1])
    
print(max(data))