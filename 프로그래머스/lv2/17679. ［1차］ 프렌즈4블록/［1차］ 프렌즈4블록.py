# 아이디어 : 완전 탐색으로 2 x 2-4개가 모두 동일하다면 인덱스를 기억해놓고 없애기
#           1. (x, y) - (x+1, y), (x, y+1), (x+1, y+1) 이 동일하다면 인덱스를 따로 기억
#           2. 바로 없앤다면 어떤 경우에는 못 찾을수도
#           3. 없앰 = 'X' 문자로 변경 (어떻게 올리지)
#           4. flag로 없앨 수 있는 블록이 있는지 없는지 비교 
#              만약 없다면 점수 return
# 알고리즘 : 브루트 포스 - O(n^3) = 30^3 = 27000
# 자료구조 

# m행 n열

def solution(m, n, board):
    answer = 0
    # board str to list
    for i in range(m) :
        board[i] = list(board[i])

    check = False # 없앨 수 있는 블록이 있는 체크
    
    while not check :
        check = True 
        explode_idx = [] # 터지는 블록 기억
        
        for x in range(m) :
            for y in range(n) :
                block = board[x][y]
                if block == '0' :
                    continue
                try :
                    if block == board[x+1][y] and block == board[x][y+1] and block == board[x+1][y+1] :
                            explode_idx.append((x, y))
                            check = False
                except IndexError :
                    continue

        for ex, ey in explode_idx :
            board[ex][ey] = '0'
            board[ex+1][ey] = '0'
            board[ex][ey+1] = '0'
            board[ex+1][ey+1] = '0'

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
        
        
    for x in range(m) :
        for y in range(n) :
            if board[x][y] == '0' :
                answer += 1
        
    return answer