# 아이디어 : 
# 알고리즘
# 자료구조 : stack

import sys
input = sys.stdin.readline

n = int(input())

stack = []
operators = []
check = True

now = 1 # 현재 숫자
for _ in range(n) :
    num = int(input())
    
    while now <= num :
        stack.append(now)
        operators.append("+")
        now += 1
    
    # stack의 top과 주어진 숫자가 같으면 pop 연산
    if stack[-1] == num :
        stack.pop()
        operators.append("-")
    # 같지 않으면
    else :
        check = False
        break
             
if not check :
    print("NO")
else :
    for op in operators :
        print(op)