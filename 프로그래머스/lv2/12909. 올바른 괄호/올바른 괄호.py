def solution(s):
    stack = []
    
    for ch in s : 
        # 열린 괄호이면 stack에 추가
        if ch == '(' :
            stack.append(ch)
        # 닫힌 괄호이면
        else :
            # 닫힌 괄호인데 stack이 비워져있다면
            if len(stack) <= 0 :
                return False
            stack.pop()
    
    # 다 탐색했는데도 stack에 요소가 있다면
    if len(stack) > 0 :
        return False
    
    return True