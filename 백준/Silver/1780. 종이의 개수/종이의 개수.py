# 아이디어: 
# 알고리즘: 분할 정복

import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

def cut(x, y, n):
    # 현재 색깔 기억
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 색깔이 다르다면
            if color != graph[i][j]:
                # 9 구역으로 나누기
                cut(x, y, n//3)
                cut(x, y + n//3, n//3)
                cut(x, y + 2 * n //3, n//3)
                
                cut(x + n//3, y, n//3)
                cut(x + n//3, y + n//3, n//3)
                cut(x + n//3, y + 2 * n //3, n//3)
                
                cut(x + 2 * n//3, y, n//3)
                cut(x + 2 * n//3, y + n//3, n//3)
                cut(x + 2 * n//3, y + 2 * n //3, n//3)
                return
    
    # 구역 내에 색깔이 모두 같다면
    result.append(color)


result = []
cut(0, 0, n)

print(result.count(-1))
print(result.count(0))
print(result.count(1))