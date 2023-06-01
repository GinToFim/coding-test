# 아이디어
# 알고리즘 : BFS
# 자료구조 : queue(deque)

from collections import deque

n = int(input())

# 시작노드 및 큐 정의
queue = deque()
queue.append((n, [n]))
visited = [False for _ in range(n + 1)]

# 큐가 빌 때까지
while queue:
    v, path = queue.popleft()
    
    # 1에 도착하였다면
    if v == 1 :
        print(len(path) - 1)
        print(*path)
        break
    
    # 한 번도 방문한 적이 없다면
    if not visited[v]:
        visited[v] = True
        
        # 3으로 나눌 수 있다면
        if v % 3 == 0:
            queue.append((v // 3, path + [v//3]))
        
        # 2로 나눌 수 있다면
        if v % 2 == 0 :
            queue.append((v // 2, path + [v//2]))
        
        # 1로 빼는 것도 추가
        queue.append((v - 1, path + [v - 1]))