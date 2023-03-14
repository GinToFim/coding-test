# 플로이드-워셜 알고리즘 : 삼중 반복문 (Dynamic Programming)
# 주대각선은 0으로

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    
# 주대각선 0으로
for a in range(1, n + 1) :
    graph[a][a] = 0
    
# 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if graph[i][j] == INF :
            print(0, end=' ')
        else :
            print(graph[i][j], end=' ')
    print()