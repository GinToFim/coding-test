import sys
input = sys.stdin.readline

n = int(input())

polygon = [list(map(int, input().split()))
        for _ in range(n)]

polygon.append(polygon[0])

result = 0

for i in range(n):
    x1, y1 = polygon[i]
    x2, y2 = polygon[i+1]

    result += x1 * y2 - x2 * y1

print(abs(result) / 2)