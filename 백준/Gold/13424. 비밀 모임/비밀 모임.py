# 아이디어 : 전체 노드중에서 이동할 수 있는 거리가 최소인 곳
# 알고리즘 : 플로이드 워셜

import sys 
input = sys.stdin.readline
INF = 10 ** 9

T = int(input())

for _ in range(T) :
    n, m = map(int, input().split())
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for _ in range(m) :
        a, b, c = map(int, input().split())
        # 양방향
        graph[a][b] = c
        graph[b][a] = c

    k = int(input())
    friends = list(map(int, input().split()))

    # 주대각선 0으로
    for a in range(1, n + 1) :
        graph[a][a] = 0

    # 플로이드-워셜 알고리즘 수행
    for k in range(1, n + 1) :
        for a in range(1, n + 1) :
            for b in range(1, n + 1) :
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    value = INF 
    result = 0

    # 모임장소가 x일 때
    for x in range(1, n + 1) :
        total = 0 # 총거리
        for friend in friends :
            total += graph[friend][x]

        # 갱신 총거리가 더 짧다면 모임장소 바꾸기
        if total < value :
            value = total
            result = x

    print(result)
        