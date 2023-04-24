# 아이디어 : 1. visited 테이블 만들기
# 알고리즘 : dfs
# 자료구조 : stack 

def solution(begin, target, words):
    answer = 10 ** 9
    
    # target이 words라는 단어 안에 없으면
    if target not in words :
        return 0
    
    # visited 테이블 만들기
    visited = [False] * len(words)
    
    def dfs(num, begin) :
        nonlocal answer
        
        # 종료 조건
        if begin == target :
            answer = min(answer, num)
            return
        
        for i in range(len(words)) :
            if not visited[i] :
                visited[i] = True
                
                cnt = 0 # 글자가 다른 것 카운트
                for ch1, ch2 in zip(begin, words[i]) :
                    if ch1 != ch2 :
                        cnt += 1

                if cnt == 1 :
                    dfs(num + 1, words[i])
                visited[i] = False

    dfs(0, begin)
    return answer