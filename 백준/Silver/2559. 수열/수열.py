# 아이디어 : k 길이의 윈도우를 슬라이딩
# 알고리즘 : 슬라이딩 윈도우

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

window = sum(data[:k])
result = window

for i in range(k, n):
    window += data[i]
    window -= data[i-k]
    result = max(result, window)
    
print(result)