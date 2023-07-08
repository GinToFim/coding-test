def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    # dfs 함수 정의
    def dfs(graph, v, visited):
        visited[v] = True # 해당 점 방문 처리
        
        for i in range(n):
            # 다른 점을 방문한 적이 없으면서 연결되어 있다면
            if not visited[i] and graph[v][i] == 1:
                dfs(graph, i, visited)
                
    for v in range(n):
        # 해당 점을 방문한 적이 없다면
        if not visited[v]:
            answer += 1
            dfs(computers, v, visited)
    
    return answer