import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, y) :
    # 범위 밖이라면 
    if x < 0 or y < 0 or x >= n or y >= m :
        return False
    
    # 방문하지 않은 곳이라면
    if graph[x][y] == 1 :
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        return True
    
    return False

T = int(input())

for _ in range(T) :
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k) :
        b, a = map(int, input().split())
        graph[a][b] = 1


    result = 0

    for i in range(n) :
        for j in range(m) :
            if dfs(i, j) == True :
                result += 1

    print(result)