# 아이디어 : (끝시간, 시작시간) 형태로 정렬
# 알고리즘 : 그리디

import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 끝시간 기준으로 정렬
meetings.sort(key = lambda x : (x[1], x[0]))

last_end = 0 # 마지막으로 끝나는 회의시간
result = 0 # 회의 가능 개수

for start, end in meetings :
    # 다음 회의가 가능하다면
    if start >= last_end :
        result += 1
        last_end = end
        
print(result)