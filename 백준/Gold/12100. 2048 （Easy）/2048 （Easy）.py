# 아이디어
# 알고리즘 : back tracking, simulation

import copy
import sys
input = sys.stdin.readline

def move(graph, step):
    # 왼쪽 이동
    if step == 'L':
        for i in range(n):
            pointer = 0
            for j in range(1, n):
                # 현재 위치가 0이 아니라면
                if graph[i][j] != 0:
                    now = graph[i][j] # 현재 위치
                    graph[i][j] = 0

                    # 포인터가 가리키는 수가 0일 때
                    if graph[i][pointer] == 0 :
                        graph[i][pointer] = now
                    # 포인터가 가리키는 수가 현재 위치와 같을 때
                    elif graph[i][pointer] == now :
                        graph[i][pointer] *= 2
                        pointer += 1 # 포인터도 다음 칸으로 넘김
                    # 포인터가 가리키는 수가 다를 때
                    else :
                        pointer += 1 # 포인터를 다음 칸으로 넘김
                        graph[i][pointer] = now # 다음 칸에 현재 숫자 대입  
                        
    # 오른쪽으로 이동
    elif step == 'R':
        for i in range(n):
            pointer = n - 1
            for j in range(n-2, -1, -1):
                if graph[i][j] != 0 :
                    now = graph[i][j]
                    graph[i][j] = 0
                    
                    if graph[i][pointer] == 0 :
                        graph[i][pointer] = now
                    elif graph[i][pointer] == now :
                        graph[i][pointer] *= 2
                        pointer -= 1 # 포인터를 반대편으로 이동!
                    else :
                        pointer -= 1
                        graph[i][pointer] = now 
                        
    # 위로 이동
    elif step == 'U':
        for j in range(n):
            pointer = 0
            for i in range(1, n):
                if graph[i][j] != 0:
                    tmp = graph[i][j]
                    graph[i][j] = 0
                    if graph[pointer][j] == 0:
                        graph[pointer][j] = tmp
                    elif graph[pointer][j]  == tmp:
                        graph[pointer][j] *= 2
                        pointer += 1
                    else:
                        pointer += 1
                        graph[pointer][j] = tmp
                        
    # 아래로 이동
    else : 
        for j in range(n):
            pointer = n-1
            for i in range(n-2, -1, -1):
                if graph[i][j] != 0 :
                    now = graph[i][j]
                    graph[i][j] = 0
                    
                    if graph[pointer][j] == 0 :
                        graph[pointer][j] = now
                    elif graph[pointer][j] == now :
                        graph[pointer][j] *= 2
                        pointer -= 1 # 포인터를 반대편으로 이동!
                    else :
                        pointer -= 1
                        graph[pointer][j] = now 
            
    return graph

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = 0

def dfs(graph, num):
    global result
    # 종료조건
    if num == 5 :
        for row in graph :
            result = max(result, max(row))
        
        return
    
    for step in ['L', 'R', 'U', 'D']:
        tmp_graph = move(copy.deepcopy(graph), step)
        dfs(tmp_graph, num + 1)
        
dfs(graph, 0)
print(result)