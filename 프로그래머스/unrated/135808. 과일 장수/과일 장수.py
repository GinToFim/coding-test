# 아이디어 : 1. score를 내림차순 정렬하기
#           2. score의 length >= m 이라면 
#              그 부분만큼 잘라서 min(p) * m 추가하기
#           3. score의 length < 이라면 finish
# 알고리즘 : greedy + sort (nlogn = 10^6 * 20 = 2 * 10 * 7)

def solution(k, m, score):
    answer = 0
    
    # score 오름차순 정렬
    score.sort()

    n = len(score)
    while n >= m :
        for _ in range(m) :
            now = score.pop()
        
        answer += now * m
        n -= m
        
        
    return answer