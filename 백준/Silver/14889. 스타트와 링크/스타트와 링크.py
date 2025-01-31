n = int(input())
board = [list(map(int, input().split()))
        for _ in range(n)]

# 방문 테이블 선언
visited = [False] * n
result = int(1e9)

def dfs(depth, start):
    global result 

    # 종료 조건 정의
    if depth == n // 2:
        # 각 팀의 능력치 초기화
        start_team = 0
        link_team = 0

        for i in range(n):
            for j in range(i + 1, n):
                # 모두 방문했다면 start 팀에 배정
                if visited[i] and visited[j]:
                    start_team += board[i][j] + board[j][i]

                # 모두 방문한 적이 없다면 link 팀에 배정
                if not visited[i] and not visited[j]:
                    link_team += board[i][j] + board[j][i]

        result = min(result, abs(start_team - link_team))
        return
    
    for i in range(start, n):
        visited[i] = True
        dfs(depth + 1, i + 1)
        visited[i] = False

dfs(0, 0)

print(result)