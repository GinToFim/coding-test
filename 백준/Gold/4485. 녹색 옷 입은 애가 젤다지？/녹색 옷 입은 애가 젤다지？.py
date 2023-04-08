# 아이디어 : 
# 알고리즘 : dijkstra (graph, distance, dx/dy)
# 자료구조 : heap(heapq)

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

def dijkstra(x, y) :
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (graph[x][y], x, y)) # (거리, x, y) 순으로 저장
    distance[x][y] = graph[x][y]
    
    # 힙큐가 빌 때까지
    while hq :
        dist, x, y = heapq.heappop(hq)
        
        # 끝지점에 도착했다면 return
        if x == n - 1 and y == n - 1 :
            return distance[x][y]
        
        # 이미 처리된 적이 있다면(기존 거리가 더 짧다면) 무시
        if distance[x][y] < dist :
                continue
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
                
            cost = dist + graph[nx][ny]
            
            # 갱신 거리가 기존 거리보다 더 짧다면
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(hq, (cost, nx, ny))
            

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# problem 카운트
cnt = 1

while True :
    n = int(input())
    
    if n == 0 :
        break

    # 그래프 입력
    graph = []
    for _ in range(n) :
        graph.append(list(map(int, input().split())))

    # 거리 테이블 초기화
    distance = [[INF] * n for _ in range(n)]

    result = dijkstra(0, 0)
    print(f'Problem {cnt}: {result}')
    cnt += 1