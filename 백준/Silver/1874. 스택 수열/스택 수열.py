# 아이디어 : 
# 알고리즘
# 자료구조 : 스택

import sys
input = sys.stdin.readline

n = int(input())
stack, operators = [], []
check = True
now = 1

for _ in range(n) :
    num = int(input())
    while now <= num :
        stack.append(now)
        operators.append('+')
        now += 1
    
    # 스택의 탑과 일치한다면
    if stack[-1] == num :
        stack.pop()
        operators.append('-')
    else :
        check = False
        break
    
if check :
    for op in operators :
        print(op)
else :
    print('NO')