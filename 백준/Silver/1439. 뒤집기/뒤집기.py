# 아이디어: 1. 연속되는 0과 1의 최소 개수 구하기
# 알고리즘: 그리디

import sys
input = sys.stdin.readline

S = input().rstrip()

# 0과 1의 그룹 count 정의 및 초기화
counter = dict()
counter['0'] = 0
counter['1'] = 0

prev = S[0]

for ch in S[1:]:
    # 현재와 이전 숫자가 다를 경우
    if ch != prev:
        counter[prev] += 1
        prev = ch
        
# 마지막 그룹 추가하기
counter[S[-1]] += 1

print(min(counter.values()))