import sys
input = sys.stdin.readline

exp = input().rstrip()

result = 0
num = 0
flag = 1

for x in exp :
    if x.isdigit():
        num = num * 10 + int(x)
    else :
        result += num * flag
        num = 0
        if x == '-':
            flag = -1
    
# 마지막 숫자도 더하기
result += num * flag
    
print(result)