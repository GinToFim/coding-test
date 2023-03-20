# 아이디어 : 1. 사다리와 뱀 입력
#           2. 1초당 좌우 1 ~ 6까지 이동
#           3. 딱 100으로 가능동안에 지나가는 시간 세기
# 알고리즘 : bfs (if visited -> O(n)=100)
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

los = dict() # 사다리와 뱀 선언

# 뱀과 사다리 입력
for _ in range(n+m) :
    x, y = map(int, input().split())
    los[x] = y

board = [0] * 101
visited = [False] * 101

def bfs(start) :
    # 시작노드 정하기
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    # 큐가 빌 때까지
    while queue :
        v = queue.popleft()
        
        # 100에 딱 도착했으면
        if v == 100 :
            return board[v]        
        
        # 1부터 6까지
        for i in range(1, 6 + 1) :
            nv = v + i
            
            # nv가 범위 이내라면
            if 1<= nv <= 100 :
                # 뱀과 사다리에 해당된다면 이동
                if nv in los.keys() :
                    nv = los[nv]
                
                # nv를 한 번도 방문하지 않았다면 갱신
                if not visited[nv] :
                    board[nv] = board[v] + 1
                    visited[nv] = True
                    queue.append(nv)

print(bfs(1))         