# 아이디어
# 알고리즘 : brute force, permutations
# 자료구조 : stack

import sys
input = sys.stdin.readline

k = int(input())
signs = list(input().split())

visited = [0 for _ in range(10)]
max_val = ""
min_val = ""

def check(x, y, sign):
    if sign == '<':
        return x < y
    else:
        return x > y

def dfs(depth, s) :
    global max_val, min_val
    
    if depth == k + 1:
        # 맨 처음 생성된 값은 최솟값
        if len(min_val) <= 0 :
            min_val = s
        # 그 이후로는 계속 대입, 최대값
        else :
            max_val = s
        
        return
    
    for i in range(10):
        if not visited[i]:
            if depth == 0 or check(int(s[-1]), i, signs[depth-1]):
                visited[i] = True
                dfs(depth+1, s+str(i))
                visited[i] = False
                
dfs(0, "")
print(max_val)
print(min_val)