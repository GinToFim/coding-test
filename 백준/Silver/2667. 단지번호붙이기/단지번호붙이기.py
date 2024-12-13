# 아이디어:
# 알고리즘: dfs
# 자료구조: stack

import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().rstrip()))
            for _ in range(n)]

def dfs(x, y):
    global cnt
    # 범위 밖이라면 종료
    if x < 0 or y < 0 or x >= n or y >= n:
        return
    
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
    

apts = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            apts.append(cnt)

# 오름차순 정렬
apts.sort()

print(len(apts))
for x in apts:
    print(x)