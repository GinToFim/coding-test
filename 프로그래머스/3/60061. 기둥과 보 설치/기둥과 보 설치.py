# 아이디어: 1. 기둥(a == 0)
#               i) 바닥 위(y == 0)
#               ii) 보의 한쪽 끝 부분 위에( (x, y, 1), (x-1, y, 1))
#               iii) 또 다른 기둥 위에 (x, y-1, 0)
#          2. 보(a == 1)
#               i) 한쪽 끝 부분이 기둥 위에 ( (x, y-1, 0), (x + 1, y-1, 0) )
#               ii) 양쪽 끝 부분이 동시에 다른 보와 연결 ( (x-1, y, 1) and (x+1, y, 1) )
# 알고리즘: 구현
# 자료구조: set (중복제거)

def solution(n, build_frame):
    answer = []
    
    for x, y, a, b in build_frame:
        # 설치라면(b = 1)
        if b == 1:
            # 우선 삽입하고
            answer.append((x, y, a))
            # 불가능하다면 다시 삭제
            if not is_possible(answer):
                answer.remove((x, y, a))
        # 삭제라면
        else:
            # 우선 삭제하고
            answer.remove((x, y, a))
            # 불가능하다면 다시 삽입
            if not is_possible(answer):
                answer.append((x, y, a))
        
    # 오름차순 정렬
    answer.sort()

    return answer

# 설치가 가능한지 확인
def is_possible(answer):
    for x, y, a in answer:
        if a == 0:  # 기둥(0)이라면
            # 해당 조건에서 설치가 가능하다면 넘김
            if y == 0 or (x, y, 1) in answer or (x-1, y, 1) in answer or (x, y-1, 0) in answer:
                continue
            
            # 아니라면 false
            return False
        else:   # 보(1)라면
            # 해당 조건에서 설치가 가능하다면 넘김
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer 
                                                                    and (x+1, y, 1) in answer) :
                continue
            
            # 아니라면 false
            return False
    
    return True