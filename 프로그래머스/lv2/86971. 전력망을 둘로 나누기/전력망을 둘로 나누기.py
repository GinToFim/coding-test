# 아이디어 : bfs + visited를 사용하여 중간 줄을 끊기
#          1. bfs 함수 설계 + visited 테이블
#          2. 특정 노드를 visited[True]로 처리하여 연결 끊기
# 알고리즘 : 그래프 탐색(bfs) + 브루트 포스
#           wires 비교: O(n^2) = 10000
# 자료구조 : queue(deque) 사용

from collections import deque

def solution(n, wires):
    answer = []
    
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for a, b in wires :
        # 양방향
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start) :
        # queue 및 start 정의
        queue = deque()
        queue.append(start)
        visited[start] = True
        cnt = 1 # 전선이 연결된 개수
        
        # queue가 빌 때까지
        while queue :
            v = queue.popleft()
            for i in graph[v] :
                if not visited[i] :
                    visited[i] = True
                    queue.append(i)
                    cnt += 1
        
        return cnt
    
    for start, not_visit in wires :
        visited = [False] * (n + 1)
        visited[not_visit] = True # 방문한 것으로 처리
        cnt = bfs(start)
        # 두 그룹의 전력망의 차이를 리스트에 append
        answer.append(abs((n-cnt) - cnt))
        
    return min(answer)