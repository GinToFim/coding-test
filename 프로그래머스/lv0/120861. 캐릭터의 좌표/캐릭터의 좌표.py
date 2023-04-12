def solution(keyinput, board):
    move_types = ['up', 'down', 'left', 'right']
    steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    
    min_x, min_y = -(board[0]//2), -(board[1]//2)
    max_x, max_y = board[0]//2, board[1]//2

    x, y = 0, 0
    for key in keyinput :
        for i in range(4) :
            if key == move_types[i] :
                nx = x + steps[i][0]
                ny = y + steps[i][1]
                # 범위 안이라면 갱신
                if min_x <= nx <= max_x and min_y <= ny <= max_y :
                    x, y = nx, ny
        
    return [x, y]