import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [x for x in range(n + 1)]

for _ in range(m) :
    i, j = map(int, input().split())
    left = i
    right = j
    
    while left <= right :
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1

print(*data[1:])