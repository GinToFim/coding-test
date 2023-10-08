# 아이디어: 1. x == -1일 때, x를 첫 글자로 초기화하고
#              x_cnt를 늘림
#          2. x != -1일 때, x_cnt와 y_cnt가 다르면 cnt 늘리기
#          3. x != -1일 때, x_cnt와 y_cnt가 같다면,
#               x를 -1로, x_cnt, y_cnt는 0으로 초기화하고
#               answer += 1
# 알고리즘: 구현, 문자열

def solution(s):
    answer = 0
    x = -1
    x_cnt = 0
    y_cnt = 0
    
    for ch in s:
        if x == -1 :
            x = ch
            x_cnt += 1
        else:
            if x == ch:
                x_cnt += 1
            else:
                y_cnt += 1
            
            if x_cnt == y_cnt:
                x = -1
                x_cnt, y_cnt = 0, 0
                answer += 1
        
    if x_cnt != 0 or y_cnt !=0 :
        answer += 1
    
    return answer