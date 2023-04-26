# 아이디어 : 무조건 딱 맞게 주어진다...? 
# 알고리즘 : 그리디 + 정렬
# 자료구조 : 

def solution(d, budget):
    answer = 0
    # 오름차순 정렬
    d.sort()
    
    for x in d :
        budget -= x 
        if budget < 0 :
            return answer
        answer += 1
    
    return answer