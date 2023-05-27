import sys
n = int(input())

x_pos = []
y_pos = []

for _ in range(n):
    x, y = map(int, input().split())
    x_pos.append(x)
    y_pos.append(y)
    
x_min, x_max = max(x_pos), min(x_pos)
y_min, y_max = max(y_pos), min(y_pos)

result = (x_max - x_min) * (y_max - y_min)
print(result)