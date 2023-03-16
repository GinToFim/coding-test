# 알고리즘 : BFS
# 자료구조 : queue(deque)

from collections import deque
MAX = 100001

n, k = map(int, input().split())
point = [-1] * MAX 

def bfs(start) :
    # 시작노드 및 큐 정의
    queue = deque()
    queue.append(start)
    point[start] = 0
    
    # 큐가 빌 때까지
    while queue :
        v = queue.popleft()
        
        # 원하는 곳에 도착했다면 return
        if v == k :
            return point[v]
        
        # v-1이 범위에 해당하고 방문하지 않았다면
        if 0 <= v - 1 < MAX and point[v - 1] == -1 :
            point[v - 1] = point[v] + 1
            queue.append(v - 1)
        
        # v*2이 범위에 해당하고 방문하지 않았다면
        if 0<= v * 2 < MAX and point[v * 2] == -1 :
            point[v * 2] = point[v]
            queue.append(v * 2)
        
        # v+1이 범위에 해당하고 방문하지 않았다면
        if 0 <= v + 1 < MAX and point[v + 1] == -1 :
            point[v + 1] = point[v] + 1
            queue.append(v + 1)
        
print(bfs(n))