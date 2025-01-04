def left(graph):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            # 현재 위치가 0이 아니라면
            if graph[i][j] != 0:
                now = graph[i][j] # 현재 값 기억
                graph[i][j] = 0

                # 포인터의 값이 0이라면 (비어있으면)
                if graph[i][pointer] == 0 :
                    graph[i][pointer] = now  # 옮기기
                # 포인터의 값과 같다면
                elif graph[i][pointer] == now :
                    graph[i][pointer] *= 2 # 합치기
                    pointer += 1 
                # 포인터의 값과 다르다면
                else :
                    pointer += 1 
                    graph[i][pointer] = now # 바로 옆에 붙이기  

    return graph

def right(graph):
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
    
    return graph

def up(graph):   
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

    return graph

def down(graph):
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

def dfs(graph, depth):
    global result
    # 종료조건
    if depth == 5 :
        for row in graph :
            result = max(result, max(row))
        
        return
    
    # 종료조건 (5번 이동했다면)
    if depth == 5:
        for row in graph:
            result = max(result, *row)

        return

    for i in range(4):
        copy_graph = [row[:] for row in graph]

        if i == 0:
            left_graph = left(copy_graph)
            dfs(left_graph, depth + 1)
        elif i == 1:
            right_graph = right(copy_graph)
            dfs(right_graph, depth + 1)
        elif i == 2:
            up_graph = up(copy_graph)
            dfs(up_graph, depth + 1)
        else:
            down_graph = down(copy_graph)
            dfs(down_graph, depth + 1)
        
dfs(graph, 0)
print(result)