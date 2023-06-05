n, m = map(int, input().split())

result = []

def dfs(num, start):
    # 종료 조건
    if num == m :
        print(*result)
        return
    
    for i in range(start, n + 1):
        result.append(i)
        dfs(num + 1, i + 1)
        result.pop()
        
dfs(0, 1)