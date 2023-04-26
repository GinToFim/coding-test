# 아이디어 : 1. 무한대, 인접 행렬 그래프 선언
#           2. 양방향
#           3. 1번 마을에서 배달까지 걸리는 시간
# 알고리즘 : floyd-warshall
# 자료구조 : 

def solution(N, road, K):
    INF = 10 ** 9
    
    graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    
    # 주대각선은 0으로
    for a in range(1, N + 1) :
        graph[a][a] = 0
    
    for rd in road :
        a, b, w = rd
        # 양방향
        graph[a][b] = min(graph[a][b], w)
        graph[b][a] = min(graph[b][a], w)
    
    # 플로이드 워셜 진행
    for k in range(1, N + 1) :
        for a in range(1, N + 1) :
            for b in range(1, N + 1) :
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    
    # 1번 마을에서 배달
    answer = [x for x in graph[1][1:] if x <= K]
    return len(answer)