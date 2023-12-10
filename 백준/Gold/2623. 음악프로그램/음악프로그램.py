# 아이디어: 1. 순서 -> 위상정렬
#           2. 보조 pd들 마다 각 노드들의 진입차수 및 순서 추가하기
#           3. 단, 각각의 간선에 대한 중복은 set로 관리
# 알고리즘: 위상정렬(graph, indegree, queue)
# 자료구조: deque(queue)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 그래프 및 진입차수 초기화
graph = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for _ in range(m):
    data = list(map(int, input().split()))
    
    for i in range(1, len(data) - 1):
        a, b = data[i], data[i+1]

        graph[a].append(b)
        indegree[b] += 1

# 위상 정렬 정의
def topology_sort():
    # 결과 테이블
    result = []
    
    # 큐 정의 및 진입차수가 0인 노드 큐에 삽입
    queue = deque()
    
    for i in range(1, n + 1):
        if indegree[i] == 0 :
            queue.append(i)
            
    # 큐가 빌 때까지
    while queue:
        now = queue.popleft()
        result.append(now)
        
        for v in graph[now]:
            # 진입차수 1 빼기
            indegree[v] -= 1
            
            # 진입차수가 0이라면 큐가 삽입
            if indegree[v] == 0 :
                queue.append(v)
        
    return result

result = topology_sort()


if sum(indegree) != 0:
    print(0)
else:
    for x in result:
        print(x)