# 아이디어
# 알고리즘 : 플로이드 워셜
# 자료구조 : 그래프 테이블

import heapq



def solution(n, s, a, b, fares):
    answer = int(1e10)
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    # 주대각선 0으로
    for x in range(1, n + 1) :
        graph[x][x] = 0
    
    for fare in fares :
        x, y, cost = fare
        graph[x][y] = cost
        graph[y][x] = cost
    
    
    # 플로이드 워셜
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
    for i in range(1, n + 1) :
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    
    return answer
