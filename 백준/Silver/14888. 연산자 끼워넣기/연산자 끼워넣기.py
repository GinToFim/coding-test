# 아이디어: 재귀적으로 풀기
# 알고리즘: dfs

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9) + 1
max_value = -int(1e9) - 1


def dfs(depth, value, add, sub, mul, div):
    global min_value, max_value
    
    # 종료조건 정의
    if depth == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return
    
    if add > 0:
        dfs(depth + 1, value + data[depth], add - 1, sub, mul, div)
    
    if sub > 0:
        dfs(depth + 1, value - data[depth], add, sub - 1, mul, div)
    
    if mul > 0:
        dfs(depth + 1, value * data[depth], add, sub, mul - 1, div)
    
    if div > 0:
        dfs(depth + 1, int(value / data[depth]), add, sub, mul, div-1)
        
dfs(1, data[0], add, sub, mul, div)

print(max_value)
print(min_value)