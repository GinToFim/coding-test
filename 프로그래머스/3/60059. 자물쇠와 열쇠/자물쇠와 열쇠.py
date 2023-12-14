# 아이디어: 1. key를 시계방향으로 90도 회전하는 함수 정의
#          2. lock의 크기를 (N X N) -> (3N X 3N)으로 늘리기 
#               (정중앙에 원래 lock 정의하기)
#          3. 자물쇠 중간이 모두 1인지 확인(딱 맞게 자물쇠를 채우기 (0과 2 X))
# 알고리즘: 구현, 완전 탐색

def solution(key, lock):
    n = len(lock)
    m = len(key)
    
    new_lock = [[0] * (3 * n) for _ in range(3 * n)]
    
    # 정중앙에 원래 lock 정의하기
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            new_lock[i][j] = lock[i-n][j-n]
    
    # new_lock 인덱스 -> x, y
    # key 인덱스 -> i, j
    
    # 4가지 방향에 대해서 확인
    for _ in range(4):
        key = rotation_90(key, m)
        
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 정확히 맞는지 확인
                if check(new_lock) == True:
                    return True
                
                # 자물쇠가 맞지 않다면 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    return False

# key(자물쇠) 시계 방향으로 90도 회전
def rotation_90(key, m):
    new_key = [[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            new_key[j][m-1 - i] = key[i][j]
            
    return new_key
    
# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    
    for i in range(lock_length, 2 * lock_length):
        for j in range(lock_length, 2 * lock_length):
            # 딱 맞지 않다면(하나라도 1이 아니라면)
            if new_lock[i][j] != 1:
                return False
            
    return True