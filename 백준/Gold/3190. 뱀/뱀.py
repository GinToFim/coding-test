# 아이디어: 1. 그래프 정의 및 사과(1)인 곳 체크하기
#           2. 뱀에 대한 정보를 큐에 저장 (이동하면서 popleft 하기)
#           3. 방향전환 steps -> [(0, 1), (1, 0), (0, -1), (-1, 0)]
#                L(왼쪽이면 -1), D(오른쪽이면 +1)
# 알고리즘: 구현, 큐
# 자료구조: queue(deque)

from collections import deque
import sys
input = sys.stdin.readline

# 그래프 입력 및 초기화
n = int(input())
graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 사과(1) 입력하기
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
# 방향 전환 시간 입력
l = int(input())
dir_dict = dict()

for _ in range(l):
    x, c = input().split()
    dir_dict[int(x)] = c

# 방향 전환 정의
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 시물레이션 함수 정의
def simulation():
    x, y = 1, 1 # 뱀의 머리 위치
    graph[x][y] = 's' # 뱀이 있는 곳은 2로 표시
    dir_idx = 0 # 처음은 동쪽
    now_time = 0 # 결과
    
    # 큐 및 시작노드 선언
    queue = deque()
    queue.append((x, y))
    
    
    while True:
        nx = x + dx[dir_idx]
        ny = y + dy[dir_idx]

        # 보드 범위 내(1~n)에 있고, 뱀이 없는 위치라면
        if 1 <= nx <= n and 1 <= ny <= n and graph[nx][ny] != 's' :
            # 사과가 없다면(0)
            if graph[nx][ny] == 0 :
                graph[nx][ny] = 's' # 머리 이동
                queue.append((nx, ny))
                # 이동하고 꼬리제거
                px, py = queue.popleft()
                graph[px][py] = 0
            # 사과가 있다면(1)
            else :
                # 머리만 이동 (꼬리 고정)
                graph[nx][ny] = 's'
                queue.append((nx, ny))
        # 벽이나 뱀에 부딪쳤다면
        else :
            now_time += 1
            return now_time
        
        # 다음 위치로 머리 이동
        x, y = nx, ny
        now_time += 1
        
        # 만약 방향 전환을 해야 하는 시간이면
        if now_time in dir_dict:
            if dir_dict[now_time] == 'L':
                dir_idx = (dir_idx - 1) % 4
            else:   
                dir_idx = (dir_idx + 1) % 4
        
result = simulation()
print(result)