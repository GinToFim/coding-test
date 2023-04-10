# 아이디어 : 벽을 비용으로 바꿔서 생각
# 알고리즘 : dijkstra (graph, distance, dx/dy)
# 자료구조 : heap(heapq)

import heapq
import sys
input = sys.stdin.readline
INF = 10 ** 9

def dijkstra(x, y) :
    # 힙큐 및 시작노드 정의
    hq = []
    heapq.heappush(hq, (graph[x][y], x, y))
    distance[x][y] = graph[x][y]
    
    # 힙큐가 빌 때까지
    while hq :
        dist, x, y = heapq.heappop(hq)

        # 목적지 도착했다면 return
        if x == n-1 and y == m-1 :
            return distance[x][y]
        
        # 이미 처리된 적이 있다면 무시
        if distance[x][y] < dist :
            continue
        
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue

            cost = dist + graph[nx][ny] 
            
            # 갱신거리가 기존거리보다 더 짧다면
            if cost < distance[nx][ny] :
                distance[nx][ny] = cost
                heapq.heappush(hq, (cost, nx, ny))

m, n = map(int, input().split())

# 벽(가중치) 테이블 정의
graph = []
for _ in range(n) :
    graph.append(list(map(int, input().rstrip())))

# 거리 테이블 정의
distance = [[INF] * m for _ in range(n)]

# 상하좌우 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
                
print(dijkstra(0, 0))