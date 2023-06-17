# 아이디어 : 
# 알고리즘 : 슬라이딩 윈도우

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
data = list(map(int, input().split()))

window = sum(data[:x])
result = window # 최대 방문자 수
cnt = 1 # 최대 방문자 수 길이

for i in range(x, n):
    window += data[i] - data[i-x]
    if window > result :
        result = window
        cnt = 1
    elif window == result :
        cnt += 1

if result == 0 :
    print("SAD")
else :
    print(result)
    print(cnt)