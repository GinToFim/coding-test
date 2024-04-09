# 아이디어: 1. 인접행렬, INF, 3중 루프 - K, 양방향
# 알고리즘: 플로이드-와샬, DP
#           O(N^3) = 10^6 -> 가능

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
data = list(map(int, input().split()))
# data = [0] + data

graph = [[INF for _ in range(n+1)] for _ in range(n + 1)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

# 주대각선은 0으로
for a in range(1, n + 1):
    graph[a][a] = 0

# 플로이드 와샬 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = -1

for row in graph[1:]:
    value = sum(x for x, d in zip(data, row[1:]) if d <= m)
    result = max(result, value)

print(result)