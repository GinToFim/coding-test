# 아이디어: 끝나는 시간을 기준으로 정렬하기
# 알고리즘: 그리디, 정렬, 활동 선택

import sys
input = sys.stdin.readline

n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준으로 오름차순 정렬
meetings.sort(key = lambda x : (x[1], x[0]))

result = 0
last_end = 0 # 마지막에 끝나는 시간

for start, end in meetings:
    # 활동이 가능하다면
    if start >= last_end:
        result += 1
        last_end = end

print(result)