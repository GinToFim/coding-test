n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(num) :
    # 종료조건
    if num == m :
        print(*result)
        return 
    
    for i in range(1, n + 1) :
        if not visited[i] :
            visited[i] = True
            result.append(i)
            dfs(num + 1)
            result.pop()
            visited[i] = False

dfs(0)