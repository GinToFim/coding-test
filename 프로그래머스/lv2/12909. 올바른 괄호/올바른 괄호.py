# 아이디어 : 1. 열린 괄호가 들어오면 스택에 담기
#          2. 닫힌 괄호가 들어오면 스택에 괄호가 있으면 O 없으면 X
#          3. 모두 탐색하고 스택에 괄호가 없으면 O, 있으면 X
# 자료구조 : stack

def solution(s):
    stack = []
    
    for ch in s :
        # 열린 괄호라면
        if ch == '(':
            stack.append(ch)
        # 닫힌 괄호라면
        else:
            # 스택이 비워져있다면
            if len(stack) <= 0 :
                return False
            
            stack.pop()

    if len(stack) > 0 :
        return False
    else :
        return True