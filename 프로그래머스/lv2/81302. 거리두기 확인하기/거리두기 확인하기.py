from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(place, x, y):
    visited = [[False] * 5 for _ in range(5)]
    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue :
        x, y, dist = queue.popleft()
        if dist >= 2:
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny]:
                    continue
                if place[nx][ny] == 'P':
                    return False
                if place[nx][ny] == 'O':
                    queue.append((nx, ny, dist + 1))
                    visited[nx][ny] = True
    return True


def solution(places):
    answer = []

    for place in places:
        check = True
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    if not bfs(place, x, y):  # 거리두기 안 지켰을 경우
                        check = False
            if not check:
                break
        
        answer.append(int(check))

    return answer