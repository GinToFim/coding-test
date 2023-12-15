# 아이디어: 1. 시계방향 90도 회전 함수 정의(rotate_90)
#          2. key를 움직이기 -> lock의 범위를 늘리기(N x N -> 3N x 3N)
#          3. new_lock  정중앙 부분에 lock 집어넣기
# 알고리즘: 구현

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    # n x n -> 3n x 3n 늘리기
    new_lock = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
    
    # 정중앙 부분에 lock 집어넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
        
    # new_lock -> i, j / key -> x, y    
    # key 4번 회전
    for _ in range(4):
        key = rotate_90(key, m)
        
        for i in range(2 * n):
            for j in range(2 * n):
                for x in range(m):
                    for y in range(m):
                        # 자물쇠에 열쇠 채워넣기
                        new_lock[i + x][j + y] += key[x][y]
                        
                # 열쇠가 딱 들어맞았다면
                if check(new_lock, n):
                    return True
                
                for x in range(m):
                    for y in range(m):
                        # 아니라면 자물쇠에 열쇠를 빼기
                        new_lock[i + x][j + y] -= key[x][y]
    
    return False

# 90도 회전 시키는 함수
def rotate_90(key, m):
    new_key = [[0] * m for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[j][m-1 - i] = key[i][j]
            
    return new_key

# 현재 자물쇠와 열쇠가 딱 들어맞았는지 확인하기
def check(new_lock, n):
    # 중앙 부분 확인하기
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            # 1이 아니라면
            if new_lock[i][j] != 1:
                return False
    
    return True
    