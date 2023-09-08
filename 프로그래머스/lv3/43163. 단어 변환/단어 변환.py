# 아이디어 : 1. visited 테이블 생성(이미 사용한 단어 중복 X)
#           2. queue에 현재 단계 과정과 현재 단어 추가(cnt, word)
#           3. 단어가 한 개만 차이난다면 변경 (queue에 append)
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(words)
    
    # visited 테이블 생성
    visited = [False for _ in range(n)]
    
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append((0, begin))
    
    # 큐가 빌 때까지
    while queue :
        depth, now_word = queue.popleft()
        
        # 정답값이 나왔다면 종료
        if now_word == target :
            return depth
        
        for i in range(n):
            # 해당 단어를 방문한 적이 없다면
            if not visited[i]:
                # 다른 알파벳 개수 세기
                diff_cnt = 0
                for ch1, ch2 in zip(now_word, words[i]):
                    if ch1 != ch2 :
                        diff_cnt += 1
            
                # 다른 알파벳 개수가 1개라면
                if diff_cnt == 1 :
                    visited[i] = True
                    queue.append((depth + 1, words[i]))
    
    
    return answer