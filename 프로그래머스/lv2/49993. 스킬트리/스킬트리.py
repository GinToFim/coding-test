# 아이디어 : 1. skill 의 문자들을 queue에 저장
#           2. skill_tree에서 만약 queue 안에 있는 ch가 나왔는데
#               A. queue[0]가 같지않다면 무시
#               B. 같다면 queue.popleft() 
# 알고리즘 : FIFO
# 자료구조 : queue (deque)

from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees :
        skill_q = deque(ch for ch in skill)
        check = True # 가능한 스킬트리인지 확인
        
        for ch in skill_tree :
            if ch in skill_q :
                if ch != skill_q[0] :
                    check = False
                    break
                else :
                    skill_q.popleft()
        
        if check :
            answer += 1
    
    return answer