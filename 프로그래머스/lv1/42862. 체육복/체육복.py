# 아이디어 : 
# 알고리즘 : 
# 자료구조 : 

# 여벌 체육복이 있는 사람이 도난당하면 못 빌려줌!
# 차집합 활용

def solution(n, lost, reserve):
    # 도난과 여벌 체육복을 동시에 있는 케이스 제거
    sub_lost = list(set(lost) - set(reserve))
    sub_reserve = list(set(reserve) - set(lost))
    
    answer = n - len(sub_lost)
    
    for lo in sub_lost :
        if lo - 1 in sub_reserve :
            sub_reserve.remove(lo - 1)
            answer += 1
        elif lo + 1 in sub_reserve :
            sub_reserve.remove(lo + 1)
            answer += 1
    
    return answer