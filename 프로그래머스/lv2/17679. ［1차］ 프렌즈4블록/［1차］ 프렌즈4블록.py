def solution(m, n, board):
    answer = 0
    # board str to list
    for i in range(m) :
        board[i] = list(board[i])

    check = False # 없앨 수 있는 블록이 있는 체크
    
    while not check :
        check = True 
        
        check, explode_list = getExplodeList(m, n, board)
        
        for ex, ey in explode_list :
            board[ex][ey] = '0'
            board[ex+1][ey] = '0'
            board[ex][ey+1] = '0'
            board[ex+1][ey+1] = '0'

        board = chagePlace(m, n, board)
        
    for x in range(m) :
        for y in range(n) :
            if board[x][y] == '0' :
                answer += 1
        
    return answer

# get 터질 블록 리스트 함수
def getExplodeList(m, n, board) :
    check = True
    explode_list = [] # 터지는 블록 기억

    for x in range(m) :
        for y in range(n) :
            block = board[x][y]
            if block == '0' :
                continue
            try :
                if block == board[x+1][y] and block == board[x][y+1] and block == board[x+1][y+1] :
                        explode_list.append((x, y))
                        check = False
            except IndexError :
                continue
    
    return check, explode_list

# 터진 자리를 올리는 함수
def chagePlace(m, n, board) :
    for y in range(n) :
        tmp_board = []
        for x in range(m) :
            # 0를 맨 앞으로 옮기기
            if board[x][y] == '0' :
                tmp_board.append(board[x][y])

        for x in range(m) :
            if board[x][y] != '0' :
                tmp_board.append(board[x][y])

        for x in range(m) :
            board[x][y] = tmp_board[x]
    
    return board