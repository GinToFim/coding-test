from itertools import combinations

def solution(relation):
    answer = 0
    
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi_list = []
    for i in range(1, col+1):
        combi_list.extend(combinations(range(col), i))
    
    # 유일성
    unique = []
    for combi in combi_list : 
        tmp = [tuple([item[x] for x in combi]) for item in relation]
        if len(set(tmp)) == row : # 유일성 체크
            check = True
            
            # unique가 비어있으면 자동으로 통과
            for x in unique : 
                if set(x).issubset(set(combi)) : # 최소성 체크
                    check = False
                    break
            
            if check :
                unique.append(combi)
        
    return len(unique)