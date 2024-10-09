# 아이디어: 
# 1. 자물쇠(lock) 가로, 세로 3배 키우기
# 2. 열쇠(key) 회전과 이동이 가능

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)

    # 3배 키운 자물쇠 정의
    new_lock = [[0 for _ in range(3*n)] for _ in range(3*n)]

    # 정중앙에 기존의 자물쇠 정의
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
        
    for _ in range(4):
        key = rotation_90(m, key)

        for i in range(2*n + 1):
            for j in range(2*n + 1):


                # 자물쇠와 키 맞춰보기
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b] += key[a][b]

                if check(n, m, key, new_lock):
                    return True

                # 자물쇠에서 키를 빼기
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b] -= key[a][b]
    
    return answer

# 현재 정중앙 부분(lock)과 키가 맞는지 확인
def check(n, m, key, new_lock):
    for x in range(n, 2*n):
        for y in range(n, 2*n):
            if new_lock[x][y] != 1:
                return False
    
    return True
    
def rotation_90(m, key):
    new_key = [[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[i][j] = key[m-1-j][i]
            
    return new_key
    
    