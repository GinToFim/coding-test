# 아이디어 : 도로는 양방향, 웜홀은 단방향
# 알고리즘 : 벨만-포드(edges, dist, cycle)

import sys

input = sys.stdin.readline
INF = 1e9


def bf(start):
    # 시작노드 정의
    dist[start] = 0

    # n번(정점의 개수)만큼 반복
    for i in range(n):
        for edge in edges:
            cur, next_node, cost = edge

            # 무한이 아니면서 갱신거리가 더 짧으면
            if dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째에서도 갱신된다면 음수 순환 존재
                if i == n - 1:
                    return True

    return False


TC = int(input())

for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []  # 간선 테이블
    # 거리 테이블 초기화
    dist = [INF for _ in range(n + 1)]

    # 도로 입력 (양방향)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

# 웜홀 입력 (단방향)
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

# 간선의 개수 = 도로*2 + 웜홀
    negative_cycle = bf(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")
