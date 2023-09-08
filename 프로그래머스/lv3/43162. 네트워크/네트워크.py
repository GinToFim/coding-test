# 아이디어 : 1. visited 테이블 생성
#           2. 해당 노드를 한 번도 방문한 적이 없다면 dfs 탐색
#           3. dfs에서 다른 노드를 방문한 적이 없으면서 연결되어 있다면
#               재귀적으로 dfs 실행
# 알고리즘 : dfs
# 자료구조 : stack(recursion)

def solution(n, computers):
    answer = 0
    # visited 테이블 생성
    visited = [False for _ in range(n)]
    
    # dfs 함수 정의
    def dfs(graph, v, visited):
        # 현재 노드는 방문 처리
        visited[v] = True
        
        for i in range(n):
            # 해당 노드를 방문한 적이 없으면서 연결되어 있다면
            if not visited[i] and graph[v][i] == 1:
                dfs(graph, i, visited)
                
    for v in range(n):
        # 해당 노드를 방문한 적이 없다면 dfs 실행과 네트워크 추가
        if not visited[v]:
            dfs(computers, v, visited)
            answer += 1
    
    return answer