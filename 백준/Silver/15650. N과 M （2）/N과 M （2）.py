# 백트래킹 정의
def dfs(num, start) :
    if num == m :
        print(*result)
        return
    
    for i in range(start, n + 1) :
        result.append(i)
        dfs(num + 1, i + 1)
        result.pop()
            

n, m = map(int, input().split())
result = []
visited = [False] * (n + 1)

# 백트래킹 실행
dfs(0, 1)