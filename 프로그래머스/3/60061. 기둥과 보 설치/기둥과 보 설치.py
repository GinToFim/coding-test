# 아이디어: 1. 설치할 때는 일단 설치하고 아니면 삭제(삭제할 때도 마찬가지)
#          2. 기둥(a == 0)일 때 다음과 같으면 가능
#               a. 바닥(y == 0)
#               b. 보의 한 쪽 끝 부분 위에 ([x-1, y, 1] or [x, y, 1])
#               c. 다른 기둥 위에 ([x, y-1, 0])
#          3. 보(a == 1)일 때 다음과 같으면 가능
#               a. 한쪽 끝 부분이 기둥 위에 ([x, y-1, 0] or [x+1, y-1, 0])
#               b. 양쪽 끝 부분이 동시에 ([x-1, y, 1] and [x+1, y, 1])
# 알고리즘: 구현

def is_possible(answer):
    for x, y, a in answer:
        # 기둥일 때
        if a == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            
            # 아니라면
            return False
        # 보일 때
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer
                                                                    and [x+1, y, 1] in answer):
                continue
            
            # 아니라면
            return False
    
    # 모두 설치가 가능하다면
    return True
        
        

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        # 삭제(0)라면 일단 삭제하고 불가능하면 다시 삽입
        if b == 0:
            answer.remove([x, y, a])
            if not is_possible(answer):
                answer.append([x, y, a])
        # 설치(1)라면 일단 삽입하고 불가능하면 다시 삭제
        else:
            answer.append([x, y, a])
            if not is_possible(answer):
                answer.remove([x, y, a])
    
    # 오름차순 정렬
    answer.sort()
    return answer