# 아이디어 :  1. combinations를 사용하여 컬럼에 대한 조합확인하기
#           2. set 자료형을 이용하여 유일성 체크 (row에 대한 길이와 비교)
#           3. issubset을 사용하여 최소성 체크
# 알고리즘
# 자료구조 : 중복(유일성, 최소성) 체크 -> set

from itertools import combinations

def solution(relation):
    row = len(relation) 
    col = len(relation[0])
    
    combi_list = []
    
    for r in range(1, col + 1) :
        for combi in combinations(range(col), r) :
            combi_list.append(tuple(combi))
            
    candidate = [] # 후보키
    
    for combi in combi_list :
        # 유일성 체크
        tmp = [tuple(item[x] for x in combi) for item in relation]
        if len(set(tmp)) != row : # 개수가 다르다면 
            continue
        
        check = True
        for x in candidate :
            if set(x).issubset(set(combi)) :
                check = False
                break
        
        if check :
            candidate.append(combi)
        
    return len(candidate)