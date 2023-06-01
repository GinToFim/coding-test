# 아이디어
# 알고리즘 : dfs, back tracking

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(depth, num, add, sub, mul, div):
    global max_value, min_value
    
    # 종료조건
    if depth == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        return
    
    if add > 0 :
        dfs(depth + 1, num + data[depth], add - 1, sub, mul, div)
        
    if sub > 0 :
        dfs(depth + 1, num - data[depth], add, sub - 1, mul, div)
        
    if mul > 0 :
        dfs(depth + 1, num * data[depth], add, sub, mul - 1, div)
        
    if div > 0 :
        dfs(depth + 1, int(num / data[depth]), add, sub, mul, div - 1)
        
dfs(1, data[0], add, sub, mul, div)
print(max_value)
print(min_value)