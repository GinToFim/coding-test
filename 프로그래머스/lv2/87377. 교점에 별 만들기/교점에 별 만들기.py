# 아이디어
# 알고리즘 : 구현

from itertools import combinations

def solution(line):
    answer = []
    points = [] # 교점을 담을 리스트
    
    # 주어진 라인 조합(nC2)
    for line1, line2 in combinations(line, 2) :
        A, B, E = line1
        C, D, F = line2
        
        try :
            x = (B * F - E * D) / (A * D - B * C)
            y = (E * C - A * F) / (A * D - B * C)

            if int(x) == x and int(y) == y :
                points.append((int(x), int(y)))
                
        # 두 직선이 평행 또는 일치하는 경우(분모가 0)
        except ZeroDivisionError :
            pass

    # 교점 중복 제거
    points = list(set(points))
    
    # x, y 최댓값, 최솟값 구하기
    x_max = max([p[0] for p in points])
    x_min = min([p[0] for p in points])
    y_max = max([p[1] for p in points])
    y_min = min([p[1] for p in points])
        
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    
    grid = [['.'] * x_len for _ in range(y_len)]
    
    for star_x, star_y in points :
        nx = star_x - x_min
        ny = star_y - y_min
        grid[ny][nx] = '*'
    
    # grid 거꾸로 하기
    for row in grid[::-1] :
        answer.append(''.join(row))
    
    return answer