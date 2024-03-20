# 아이디어 : 1. 그래프, 상하좌우 정의
#            2. 그래프의 해당 지역의 배추(1)가 있을 경우 dfs 탐색
#            3. 지역만큼 +1
# 알고리즘 : bfs
# 자료구조 : stack

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# dfs 함수 정의
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    
    # 해당 노드에 배추(1)가 있다면
    if graph[x][y] == 1 :
        # 해당 노드 방문 처리
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    
    # 배추가 아니라면
    return False

T = int(input())

for _ in range(T):
    # 그래프 정의
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    # 상하좌우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 배추 구역 세기
    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True :
                cnt += 1

    print(cnt)