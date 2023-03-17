n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(start, num) :
    # 종료 조건
    if num == m :
        print(*result)
        return
    
    for i in range(start, n + 1) :
        if not visited[i] :
            visited[i] = True
            result.append(i)
            dfs(i, num + 1)
            result.pop()
            visited[i] = False

dfs(1, 0)