def gradient(dots, line) :
    dot1, dot2 = dots[line[0]], dots[line[1]]
    x1, y1 = dot1
    x2, y2 = dot2
    
    return (y1 - y2) / (x1 - x2)

def solution(dots):
    answer = 0
    
    line_cases = [[(0, 1), (2, 3)], [(0, 2), (1, 3)],[(0, 3), (1, 2)]]
    
    for line_case in line_cases :
        line1, line2 = line_case
        
        if gradient(dots, line1) == gradient(dots, line2):
            return 1
    else :
        return 0
    