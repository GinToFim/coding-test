# 아이디어: [1, 2, 3, 1]을 찾으면 그만큼 없애기
# 알고리즘: 브루트 포스 

def solution(ingredient):
    answer = 0
    idx = 0
    while True:
        # 현재길이가 범위이내라면
        if idx > len(ingredient) - 4:
            break

        if ingredient[idx:idx+4] == [1, 2, 3, 1]:
            answer += 1
            ingredient = ingredient[:idx] + ingredient[idx+4:]
            idx -= 2  
        
        idx += 1
    return answer