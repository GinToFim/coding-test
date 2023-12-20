# 아이디어:
# 알고리즘: 

def solution(p):
    answer = ''
    # 1. 입력이 빈 문자열인 경우, 빈 문자열 반환
    if len(p) == 0 :
        return ""
    
    # 2. 문자열 p를 두 '균형잡힌 괄호 문자열' u, v로 나누기
    idx = balanced_index(p)
    u = p[:idx + 1]
    v = p[idx + 1:]
    
    # 3. '올바른 괄호 문자열'이라면 v 붙이기
    if is_right(u):
        answer = u + solution(v)
    # 4. 아니라면
    else:
        answer = '(' # 4-1. 빈 문자열에 '(' 붙이기
        answer += solution(v) # 4-2. v에 대해 재귀적으로 실행
        answer += ')' # 4-2. ')'를 다시 붙이기
        
        # 4-4. 첫 번째와 마지막 문자 제거
        u = list(u[1:-1])
        
        # 나머지 문자열의 괄호 방향 뒤집어 붙이기
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        
        answer += "".join(u)
        
    return answer

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    open_count, close_count = 0, 0
    
    for i in range(len(p)):
        # 열린 괄호라면
        if p[i] == '(':
            open_count += 1
        # 닫힌 괄호라면
        else:
            close_count += 1
    
        # 열린 괄호와 닫힌 괄호가 같다면 현재 인덱스 반환
        if open_count == close_count:
            return i
        
# 해당 괄호가 올바른지 확인
def is_right(u):
    count = 0 # 열린 괄호 개수
    
    for ch in u:
        # 열린 괄호라면
        if ch == '(':
            count += 1
        else:
            # 쌍이 맞지 않는 경우 false
            if count == 0:
                return False
            
            count -= 1
    
    # 모두 탐색 후에도 스택에 자료가 남았다면
    if count != 0:
        return False
    
    return True
        
        
    