def solution(board):
    n = len(board)
    # 상하좌우 대각선, 8방
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1),
             (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # 지뢰 위치 표시
    mines = []
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                mines.append((i, j))
                
    for mine in mines :
        x, y = mine
        for step in steps :
            nx = x + step[0]
            ny = y + step[1]
            
            # 범위 밖이라면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n :
                continue
            
            # 위험 지역으로 변경
            board[nx][ny] = 1
    
    # 위험지역 개수 세기
    num = sum([sum(row) for row in board])
    return n * n - num