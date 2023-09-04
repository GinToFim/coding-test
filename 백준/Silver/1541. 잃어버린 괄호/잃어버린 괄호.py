# 아이디어 : '-'가 나오는 순간 전부 음수 처리
# 알고리즘 : 그리디

import sys
input = sys.stdin.readline

data = input().rstrip()

result = 0
flag = 1
num = 0

for x in data :
    if x == '-':
        result += num * flag
        flag = -1
        num = 0
    elif x == '+':
        result += num * flag
        num = 0
    else :
        num = num * 10 + int(x)

# 마지막 더하기
result += num * flag
print(result)