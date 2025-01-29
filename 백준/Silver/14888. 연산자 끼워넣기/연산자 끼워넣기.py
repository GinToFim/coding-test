n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e10)
min_val = int(1e10)

def dfs(depth, num, add, sub, mul, div):
    global max_val, min_val
    
    # 종료조건 정의
    if depth == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
        return

    if add > 0:
        dfs(depth + 1, num + data[depth], add-1, sub, mul, div)
    
    if sub > 0:
        dfs(depth + 1, num - data[depth], add, sub-1, mul, div)
    
    if mul > 0:
        dfs(depth + 1, num * data[depth], add, sub, mul-1, div)
    
    if div > 0:
        dfs(depth + 1, int(num / data[depth]), add, sub, mul, div-1)
    
dfs(1, data[0], add, sub, mul, div)

print(max_val)
print(min_val)