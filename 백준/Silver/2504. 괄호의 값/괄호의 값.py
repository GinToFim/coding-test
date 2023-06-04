# 아이디어 : 1. 열린 괄호가 나오면 곱하기
#           2. 닫힌 괄호가 나오면 
#                첫 번째 닫힌 괄호면 result에 더하고 나누기
#                두 번째 이후 닫힌 괄호면 나누기
#           3. stack의 top의 닫힌괄호와 열린괄호가 맞지 않으면 0
#              for 문을 다 돌고 stack의 요소가 남아 있으면 0
# 알고리즘 : implementation
# 자료구조 : stack - 

import sys
input = sys.stdin.readline

brackets = input().rstrip()

result = 0
now = 1
stack = []

for i in range(len(brackets)):
    # 열린 괄호일 때
    if brackets[i] == '(':
        now *= 2
        stack.append('(')
    elif brackets[i] == '[':
        now *= 3
        stack.append('[')
    # 닫힌 괄호일 때
    elif brackets[i] == ')':
        # stack의 요소가 없거나 stack의 top이 열린 괄호가 아니라면
        if len(stack) <= 0 or stack[-1] != '(':
            result = 0
            break
        
        # 바로 이전이 열린 괄호이면
        if brackets[i-1] == '(':
            result += now
        
        stack.pop()
        now //= 2
    else:
        # stack의 top이 열린 괄호가 아니라면
        if len(stack) <= 0 or stack[-1] != '[':
            result = 0
            break
        
        # 바로 이전이 열린 괄호이면
        if brackets[i-1] == '[':
            result += now
        
        stack.pop()
        now //= 3

# stack의 요소가 남아있다면
if len(stack) > 0 :
    result = 0
    
print(result)