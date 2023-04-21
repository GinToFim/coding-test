# 아이디어 : 1. bfs로 돌면서 해당 숫자를 추가함
#           2. 도는 와중에 X로 바꾸기
# 알고리즘 : bfs(maps, dx/dy)
# 자료구조 : queue(deque)

from collections import deque

def solution(maps):
    answer = []
    
    # maps를 리스트로 바꾸기
    maps = [[x for x in map] for map in maps]
    print(maps)
    
    n = len(maps)    # 행의 길이
    m = len(maps[0]) # 열의 길이
    
    
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(x, y) :
        # 시작노드 및 큐 정의
        queue = deque()
        queue.append((x, y))
        cnt = int(maps[x][y])
        maps[x][y] = 'X'
        
        # 큐가 빌 때까지
        while queue :
            x, y = queue.popleft()
            
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 밖이라면 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m :
                    continue
                
                # 지나갈 수 있다면
                if maps[nx][ny] != 'X' :
                    cnt += int(maps[nx][ny])
                    maps[nx][ny] = 'X'
                    queue.append((nx, ny))
        
        # 최종적인 cnt return
        return cnt
    
    for a in range(n) :
        for b in range(m) :
            if maps[a][b] != 'X' :
                answer.append(bfs(a, b))
    
    if len(answer) <= 0 :
        return [-1]
    else :
        answer.sort()
        return answer