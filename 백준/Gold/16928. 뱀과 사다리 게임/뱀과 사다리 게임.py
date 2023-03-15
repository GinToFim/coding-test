# 아이디어 : 0. 100칸을 초과했다면 무시
#           1. 사다리(ladder), 뱀(snake)을 dictionary로 선언 
#           2. x + 1 ~ x + 6으로 queue append하기
# 알고리즘 : bfs
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = dict() # 사다리 선언
snake = dict() # 뱀 선언

board = [0] * 101
visited = [False] * 101

# 사다리 입력
for _ in range(n) :
    u, v = map(int, input().split())
    ladder[u] = v

# 뱀 입력
for _ in range(m) :
    u, v = map(int, input().split())
    snake[u] = v
    
def bfs(start):
    cnt = 0 # 주사위를 던진 횟수
    
    queue = deque()
    queue.append(start) # (위치, 횟수)순으로 저장
    
    # queue 가 빌 때까지
    while queue :
        v = queue.popleft()
        
        # 100에 도착했다면 return
        if v == 100 :
            return board[v]
        
        for i in range(1, 6 + 1) :
            nv = v + i 
            
            # 100을 초과했거나 이미 방문한 적이 있다면 무시
            if nv > 100 or visited[nv] :
                continue
            
            # 사다리에 해당하면 변환
            if nv in ladder.keys() :
                nv = ladder[nv]
            
            # 뱀에 해당하면 변환
            if nv in snake.keys() :
                nv = snake[nv]
            
            # 해당 칸을 한번도 방문한 적이 없다면
            if not visited[nv] :
                board[nv] = board[v] + 1
                visited[nv] = True
                queue.append(nv)

print(bfs(1))