# 알고리즘 : bfs
# 자료구조 : deque

from collections import deque

n, k = map(int, input().split())
board = [-1] * 100001

def bfs(x) :
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append(x)
    board[x] = 0
    
    # 큐가 빌 때까지
    while queue :
        v = queue.popleft()
        
        if v == k :
            return board[v]
        
        for nv in (v - 1, v + 1, 2 * v) :
            # 범위 이내이고 방문한 적이 없다면
            if 0 <= nv <= 100000 and board[nv] == -1 :
                board[nv] = board[v] + 1
                queue.append(nv)
                
print(bfs(n))