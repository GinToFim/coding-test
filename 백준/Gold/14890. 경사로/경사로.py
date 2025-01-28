n, l = map(int, input().split())

board = [list(map(int, input().split()))
        for _ in range(n)]

row = board[0]

def check(line, l):
    # 경사 방문 테이블 선언
    visited = [False] * (n + 1)

    for i in range(n-1):
        # 현재 경사와 다음 경사가 높이가 같다면
        if line[i] == line[i+1]:
            continue
        # 높이 차이가 1보다 크다면
        elif abs(line[i] - line[i+1]) > 1:
            return False
        # 현재 높이가 다음 높이보다 크다면
        if line[i] > line[i+1]:
            temp = line[i+1]

            for j in range(i+1, i+l+1):
                # 범위 안이라면
                if 0 <= j < n:
                    # 경사를 놓을 크기가 하나라도 다르면
                    if line[j] != temp:
                        return False
                    # 이미 방문한 적이 있다면
                    elif visited[j]:
                        return False
                    visited[j] = True
                # 범위 밖이라면
                else:
                    return False
        # 다음 높이가 현재 높이보다 크다면
        else:
            temp = line[i]

            for j in range(i, i-l, -1):
                # 범위 안이라면
                if 0 <= j < n:
                    # 경사를 놓을 크기가 하나라도 다르면
                    if line[j] != temp:
                        return False
                    # 이미 방문한 적이 있다면
                    elif visited[j]:
                        return False
                    visited[j] = True
                # 범위 밖이라면
                else:
                    return False

    return True


result = 0
for row in board:
    if check(row, l):
        result += 1

for j in range(n):
    col = [board[i][j] for i in range(n)]
    if check(col, l):
        result += 1

print(result)