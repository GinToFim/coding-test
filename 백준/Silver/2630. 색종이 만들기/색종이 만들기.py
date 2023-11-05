# 아이디어: 1. 같은 구역내에 색깔이 다르다면 그 구역을 4구역으로 나누기 
# 알고리즘: 분할 정복

import sys
input = sys.stdin.readline

def cut(x, y, n):
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색깔이 다르다면
            if color != graph[i][j]:
                # 4개의 구역으로 나누기
                cut(x, y, n//2)
                cut(x, y + n//2, n//2)
                cut(x + n//2, y, n//2)
                cut(x + n//2, y + n//2, n//2)
                return # 색깔이 다르다면 구역을 나누고 종료
    
    # 같은 구역 내에 색깔이 모두 같다면
    result.append(color)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = []
cut(0, 0, n)

# 하얀색(0) 출력
print(result.count(0))
# 파란색(1) 출력
print(result.count(1))