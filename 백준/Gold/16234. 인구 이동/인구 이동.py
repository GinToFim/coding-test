# 아이디어 : 1. 인구의 차이가 L이상이고 R이하 일 때 탐색
#          2. visited 리스트를 만들어서 이미 방문한 적이 있는지 체크
#          3. 하나라도 국경선이 열려있으면 check = True (default : check=False)
#          4. united 리스트 안에 열려있는 나라(x, y) 담기
# 알고리즘 : bfs (graph, visited, dx/dy)
# 자료구조 : queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y) :
    # 큐 및 시작노드 정의
    queue = deque()
    united = [] # 연합 국가 리스트
    
    visited[x][y] = True
    queue.append((x, y))
    united.append((x, y)) 
    
    # 큐가 빌 때까지
    while queue :
        x, y = queue.popleft()
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            
            # 방문한 적이 없고 인구 차이가 이내라면
            if not visited[nx][ny] and l <= abs(graph[x][y] - graph[nx][ny]) <= r :
                visited[nx][ny] = True
                queue.append((nx, ny))
                united.append((nx, ny))
    
    return united


n, l, r = map(int, input().split())
graph = []

for _ in range(n) :
    graph.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0 # 날짜수

while True :
    
    # 방문 테이블
    visited = [[False] * n for _ in range(n)] 
    check = False # 연합 국가가 있는지 체크 
    
    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                united = bfs(i, j)
                if len(united) > 1 :
                    check = True
                    
                    # 연합 국가 인구 계산
                    number = sum([graph[x][y] for x, y in united]) // len(united)
                    
                    for x, y in united :
                        graph[x][y] = number

    # 연합한 국가가 하나라도 없으면 break
    if not check :
        break
                    
    result += 1   

print(result)