def solution(dots):
    max_x, max_y = -257, -257
    min_x, min_y = 257, 257
    
    for dot in dots :
        x, y = dot
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        
    return (max_x - min_x) * (max_y - min_y)