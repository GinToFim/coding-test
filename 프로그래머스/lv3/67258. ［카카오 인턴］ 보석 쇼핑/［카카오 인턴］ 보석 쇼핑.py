# 아이디어 : 0. set로 종류 카운트, dict로 종류와 개수 카운트
#           1. start, end 모두 gem의 길이보다 작을 때까지 while
#           2. 종류가 부족하면 end 증가, 종류가 같거나 많으면 start 증가

# 알고리즘 : 투포인터 (start, end) - O(2n)
# 자료구조 : set, dict

def solution(gems):
    n = len(gems)
    answer = [0, n-1]
    
    kind = len(set(gems)) # 종류 개수
    gems_dict = dict()  # 딕셔너리 초기화
    gems_dict[gems[0]] = 1 
    
    start, end = 0, 0 # 투포인터 초기화
    
    # start와 end가 n 전까지
    while start < n and end < n :
        if len(gems_dict) < kind : # 종류가 부족하면 end와 dict 개수 증가
            end += 1
            if end == n : 
                break
            gems_dict[gems[end]] = gems_dict.get(gems[end], 0) + 1
        
        else : # 종류가 같거나 많으면 start 증가, dict 개수 감소
            if (end - start) < (answer[1] - answer[0]) : # answer 갱신
                answer = [start, end]
            
            if gems_dict[gems[start]] == 1 :
                del gems_dict[gems[start]]
            else :
                gems_dict[gems[start]] -= 1
        
            start += 1
                
    answer[0] += 1
    answer[1] += 1
    return answer