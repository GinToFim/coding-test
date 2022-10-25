# 2차원 리스트 90도 회전
def rotate_90(arr) :
    n = len(arr) # 행 길이
    m = len(arr[0]) # 열 길이
    result = [[0] * n for _ in range(m)] # 90도 회전한 리스트
    
    for i in range(n) :
        for j in range(m) :
            result[j][n-i-1] = arr[i][j]
            
    return result

def check(new_lock) :
    lock_length = len(new_lock) // 3 # 기존 자물쇠 길이
    
    for i in range(lock_length, lock_length * 2) :
        for j in range(lock_length, lock_length * 2) :
            if new_lock[i][j] != 1 :
                return False
    
    return True


def solution(key, lock):
    n = len(lock) # 자물쇠 크기
    m = len(key)  # 열쇠 크기
    
    # 자물쇠의 크기를 기존의 3배로 전환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # 3배로 커진 새로운 자물쇠의 중앙 부분에 기존 좌물쇠 넣기
    for i in range(n) :
        for j in range(n) :
            new_lock[i + n][j + n] = lock[i][j]
            
    # 열쇠 4가지 방향에 대해서 확인 [90, 180, 270, 360]
    for _ in range(4) : 
        key = rotate_90(key)
        
        # 자물쇠에 열쇠 넣기
        # x, y : 자물쇠에 대한 인덱스
        for x in range(n * 2) :
            for y in range(n * 2) :
                # i, j : 열쇠에 대한 인덱스
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 맞는지 체크
                if check(new_lock) :
                    return True
                
                # 틀리다면 자물쇠에서 열쇠 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
    
    # 열쇠를 4방향 돌렸음에도 안맞다면 없음
    return False