# 아이디어 : 
# 알고리즘 : 
# 자료구조 : queue(deque) 사용

from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees :
        queue = deque(skill)
        v = queue.popleft()
        check = True
        idx = 0
        
        # 큐가 빌 때까지
        while queue and idx < len(skill_tree):
            if v != skill_tree[idx] :
                if skill_tree[idx] in queue : 
                    check = False
                    break
            else :
                v = queue.popleft()

            idx += 1

        if check :
            answer += 1
            
    return answer