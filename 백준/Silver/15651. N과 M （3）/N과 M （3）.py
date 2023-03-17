n, m = map(int, input().split())

result = []

def dfs(num) :
    if num == m :
        print(*result)
        return
    
    for i in range(1, n + 1) :
        result.append(i)
        dfs(num + 1)
        result.pop()

dfs(0)