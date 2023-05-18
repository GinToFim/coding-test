# 아이디어 : 1. '('이면 stack에 요소를 담고 tmp * 2
#           2. ')'일 때,
#                a. stack이 빈 리스트이거나, stack의 top이 '('가 아니라면 0
#                b. bracket의 바로 전이 '('이면 result에 더하기
#                c. 아니라면 통과
#                d. 다시 tmp //= 2
# 알고리즘 : X
# 자료구조 : stack (list)

import sys
input = sys.stdin.readline

bracket = input().rstrip()

stack = [] # 괄호 상황을 담을 리스트
result = 0 # 결과 
tmp = 1 # 초기값

for i in range(len(bracket)) :
    # 여는 괄호이면
    if bracket[i] == '(':
        tmp *= 2
        stack.append('(')
    elif bracket[i] == '[':
        tmp *= 3
        stack.append('[')
    
    # 닫는 괄호이면
    elif bracket[i] == ')':
        # 빈 스택이거나 top이 여는 괄호가 아니라면
        if not stack or stack[-1] != '(' :
            result = 0
            break
        
        # 이전 원소가 해당 여는 괄호라면
        if bracket[i-1] == '(' : 
            result += tmp
        tmp //= 2
        stack.pop()
    else :
        # 빈 스택이거나 top이 여는 괄호가 아니라면
        if not stack or stack[-1] != '[' :
            result = 0
            break
        
        # 이전 원소가 해당 여는 괄호라면
        if bracket[i-1] == '[' : 
            result += tmp
        tmp //= 3
        stack.pop()
    
# 스택이 빈 리스트가 아니라면
if stack :
    print(0)
else :
    print(result)