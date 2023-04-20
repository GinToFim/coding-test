# 아이디어 : 1. visited 테이블 만들기 (-1이 방문 X)
#          2. (n 더하기) or (2 곱하기) or (3 곱하기) 를 한꺼번에 탐색
#          3. 가장 빨리 y에 도착한 횟수를 return
# 알고리즘 : bfs(visited, n, *2, *3)
# 자료구조 : queue(deque)

from collections import deque

def solution(x, y, n):
    answer = 0
    visited = [-1 for _ in range(y + 1)]
    
    def bfs(x) :
        # 큐 및 시작노드 정의
        queue = deque()
        queue.append(x)
        visited[x] = 0
        
        # 큐가 빌 때까지
        while queue :
            v = queue.popleft()
            
            # 목적지에 도착했다면
            if v == y :
                return visited[v]
        
            for nv in (v + n, 2 * v, 3 * v) :
                
                # 범위 밖이라면 무시
                if nv > y :
                    continue

                # 방문한 적이 없다면 횟수 추가
                if visited[nv] == -1 :
                    visited[nv] = visited[v] + 1
                    queue.append(nv)
        
        # 도착할 수 없다면
        return -1
        
    return bfs(x)