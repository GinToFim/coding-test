# 알고리즘: 구현

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0:
        return ""
    
    # 2. 두 균형잡힌 괄호 문자열 u, v로 분리
    idx = balanced_index(p)
    
    u = p[:idx+1]
    v = p[idx+1:]
    
    # 3. u가 "올바른 괄호 문자열"이라면
    if is_right(u):
        return u + solution(v) # v에 대해 재귀적으로 실행
    # 4. u가 "올바른 괄호 문자열" 아니라면
    else:
        # 4-1. 빈 문자열에 '('를 붙이기
        answer = "("
        
        # 4-2. 문자열 v에 대해 재귀적으로 실행
        answer += solution(v)
        
        # 4-3. ')'를 다시 붙이기
        answer += ')'
        
        # 4-4. u의 첫 번째와 마지막 문자를 삭제하고, 나머지 문자열의 괄호 방향 뒤집기 
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        # 4-5. 생성된 문자열을 반환
        return answer + ''.join(u)
        
        
    
    
    
    
    return answer

# '균형잡힌 괄호 문자열' 체크 함수
def balanced_index(w):
    # 열린 괄호, 닫힌 괄호 개수
    open_cnt, close_cnt = 0, 0
    
    for i in range(len(w)):
        # 열린 괄호라면
        if w[i] == '(':
            open_cnt += 1
        # 닫힌 괄호라면
        else:
            close_cnt += 1
        
        # 열린 괄호와 닫힌 괄호의 개수가 같다면
        if open_cnt == close_cnt:
            return i
        
# "올바른 괄호 문자열" 구하는 함수
def is_right(u):
    open_cnt = 0 # 열린 괄호 개수
    
    for ch in u:
        # 열린 괄호라면
        if ch == '(':
            open_cnt += 1
        # 닫힌 괄호라면
        else:
            # 열린 괄호가 이미 없다면
            if open_cnt == 0:
                return False
            
            open_cnt -= 1
    
    # "올바른 괄호"라면
    return True
        
        
        
        