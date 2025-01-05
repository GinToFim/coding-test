import math

n = int(input())
data = list(map(int, input().split()))
b, c = map(int, input().split())

# 총감독관이 감시할 수 응시자만큼 빼기
data = [x - b for x in data]

result = len(data)

for x in data:
    if x > 0:
        result += math.ceil(x / c)

print(result)