import sys
input = sys.stdin.readline
INF = int(1e9)

# 벨만-포드 알고리즘 정의
def bf(start) :
    # 시작노드 초기화
    dist[start] = 0
    
    # 전체 n번(정점의 개수)의 라운드를 반복
    for i in range(n) :
        # 매 반복마다 "모든 간선"을 확인
        for j in range(m) :
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            
            # 현재 거리보다 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost :
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1 :
                    return True
    
    return False


# 노드의 개수, 간선의 개수를 입력
n, m = map(int, input().split())

edges = [] # 간선 리스트
dist = [INF] * (n + 1) # 최단 거리 테이블을 무한으로 초기화

# 모든 간선 정보 입력
for _ in range(m) :
    a, b, c = map(int, input().split())
    edges.append((a, b, c)) # a에서 b로 가는 비용 c라는 의미
    
# 벨만-포드 알고리즘 수행
negative_cycle = bf(1)

if negative_cycle :
    print("-1")
else :
    # 1번노드 제외 출력
    for i in range(2, n + 1) :
        # 도달할 수 없는 거리라면
        if dist[i] == INF :
            print(-1)
        else :
            print(dist[i])