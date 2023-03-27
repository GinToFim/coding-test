# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque

n = int(input())

# bfs 테이블 선언
board = [0] * (n + 1)

def bfs(n) :
    # 큐 및 시작노드 정의
    queue = deque()
    queue.append(n)

    # 큐가 빌 때까지
    while queue :
        v = queue.popleft()
        
        # 1에 도착했다면 return
        if v == 1 :
            return board[v]

        # 2로 나눌 수 있고 아직 방문 전이라면
        if v % 2 == 0 and board[v//2] == 0 :
            board[v//2] = board[v] + 1
            queue.append(v//2)
        
        if v % 3 == 0 and board[v//3] == 0 :
            board[v//3] = board[v] + 1
            queue.append(v//3)
        
        # 1을 빼기 추가
        if board[v-1] == 0 :
            board[v-1] = board[v] + 1
            queue.append(v-1)
        
        
print(bfs(n))
