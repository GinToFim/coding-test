# 아이디어 : 1. 각 line들을 100씩 더하기 (-100 ~ 100 -> 0 ~ 200 구간 변경)
#           2. 0 ~ 200만큼의 리스트 만들기
#           3. 각 line들의 범위만큼 1씩 더하기
#           4. 리스트에 cnt가 2 이상이면 카운트
# 알고리즘 : brute force

def solution(lines):
    answer = 0
    # 0 ~ 200의 범위 리스트
    bounds = [0 for _ in range(201)] 
    
    for line in lines :
        a, b = line
        a, b = a + 100, b + 100
        
        for i in range(a, b) :
            bounds[i] += 1
    
    for i in range(201) :
        if bounds[i] >= 2 :
            answer += 1
    
    return answer