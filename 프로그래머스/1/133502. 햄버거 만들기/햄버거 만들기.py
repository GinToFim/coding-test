# 아이디어: [1, 2, 3, 1]을 찾으면 그만큼 없애기
# 알고리즘: 브루트 포스
# 자료구조: 스택

def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            
            for _ in range(4):
                stack.pop()
    
    return answer