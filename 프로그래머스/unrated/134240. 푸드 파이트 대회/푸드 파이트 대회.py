# 아이디어: 1. 물(0)은 항상 1
#          2. food[1:] 짝수로 나누기
# 알고리즘: 구현

def solution(food):
    answer = ''
        
    for i in range(1, len(food)):
        answer += str(i) * (food[i] // 2)
    
    return answer + '0' + answer[::-1]