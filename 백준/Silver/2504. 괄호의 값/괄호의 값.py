# 아이디어 : 1. 열린 괄호라면 stack에 push, 해당 수만큼 tmp에 곱하기
#           2. 닫힌 괄호라면
#              a. 바로 앞이 해당 열린 괄호라면 result에 추가
#              b. 아니라면 나누기
# 자료구조 : 스택

bracket = input()

stack = []
result = 0
now = 1


for i in range(len(bracket)):
    # 열린 괄호라면
    if bracket[i] == '(':
        now *= 2
        stack.append('(')
    elif bracket[i] == '[':
        now *= 3
        stack.append('[')
    # 닫힌 괄호라면
    elif bracket[i] == ')':
        # stack 안에 원소가 없으면서 top이 해당 열린 괄호가 아니라면
        if not stack or stack[-1] != '(' :
            result = 0
            break
        # 바로 이전이 열린괄호라면
        if bracket[i-1] == '(': 
            result += now

        now //= 2
        stack.pop()
    else :
        if not stack or stack[-1] != '[' :
            result = 0
            break
        if bracket[i-1] == '[': 
            result += now

        now //= 3
        stack.pop()
    
# 스택에 원소가 있다면
if stack : 
    print(0)
else :
    print(result)