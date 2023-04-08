# 아이디어 : 1. 양방향
#           2. 전체 노드를 뒤지는데 수색범위가 가능하면 아이템 갖기
#           3. 전체 노드에서 떨어지는데 그 중에서 최대 아이템 갖는 것 max 찾기
# 알고리즘 : 플로이드-워셜 (O(n^3) = 1000,000), 브루트 포스

import sys
input = sys.stdin.readline
INF = 10 ** 9

n, m, r = map(int, input().split())
items = list(map(int, input().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(r) : 
    a, b, l = map(int, input().split())
    # 양방향
    graph[a][b] = l
    graph[b][a] = l
    
# 주대각선 0으로
for x in range(1, n + 1) :
    graph[x][x] = 0
    
# 플로이드-워셜 수행
for k in range(1, n + 1) :
    for x in range(1, n + 1) :
        for y in range(1, n + 1) :
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

result = 0

for i in range(1, n + 1) :
    cnt = 0 # 현재 아이템 개수
    for j in range(1, n + 1) :
        # 수색이 가능하다면
        if graph[i][j] <= m :
            cnt += items[j-1]
            
    result = max(result, cnt)

print(result)