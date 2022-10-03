# 아이디어 : 
# 1. 앞서 나온 단어를 기억하고 있어야 함 -> dict 저장
# 2. 단어의 맨 앞과 맨 끝을 비교 (끝말잇기)
# 3. n번 사람(num), n번 차례(times)

# 알고리즘 : 최대 O(n^2) => 10000 
# 자료구조 : 해시-맵 사용

def solution(n, words):
    answer = []

    # 모든 단어 False로 초기화
    check = dict()
    for word in words :
        check[word] = False
    
    # 첫 번째 단어는 바로 실행
    num, times = 1, 1
    check[words[0]] = True
    
    for i in range(1, len(words)) :
        num += 1
        if num > n :
            num = 1
            times += 1
        
        # 끝말잇기가 틀렸다면
        if words[i][0] != words[i-1][-1] :
            answer.append(num)
            answer.append(times)
            return answer
        
        # 이미 썻던 단어라면 
        if check[words[i]] == True :
            answer.append(num)
            answer.append(times)
            return answer
        
        # 통과한 단어 체크 표시
        check[words[i]] = True
    
    # for문을 탈출했다면(주어진 단어로 끝말잇기가 끝났다면)
    return [0, 0]