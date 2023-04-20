# 아이디어 : 1. graph는 가중치로, distance는 무한대로 초기화
#           2. 
# 알고리즘 : dijkstra(graph, dx/dy, distance)
# 자료구조 : heapq

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(x, y) :
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (graph[x][y], x, y)) # (거리, x, y)순으로 저장
    distance[x][y] = graph[x][y]
    
    # 힙큐가 빌 때까지
    while hq :
        dist, x, y = heapq.heappop(hq)
        
        # 목적지에 도착했다면
        if x == n-1 and y == n-1 :
            return distance[x][y]
        
        # 만약 현재 거리가 이미 처리된 적이 있다면
        if distance[x][y] < dist :
            continue
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            
            cost = dist + graph[nx][ny]
            # 갱신거리가 기존거리보다 짧다면
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(hq, (cost, nx, ny))
                
idx = 1      
while True :
    n = int(input())
    
    if n == 0 :
        break
    
    graph = []
    
    for _ in range(n) :
        graph.append(list(map(int, input().split())))
    
    distance = [[INF for _ in range(n)] for _ in range(n)]
    
    result = dijkstra(0, 0)
    print(f'Problem {idx}: {result}')
    idx += 1