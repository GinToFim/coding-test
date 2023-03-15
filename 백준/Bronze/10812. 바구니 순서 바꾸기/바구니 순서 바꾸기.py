import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [x for x in range(n + 1)]

for _ in range(m) :
    begin, end, mid = map(int, input().split())
    new = data[:begin] + data[mid:end+1] + data[begin:mid] + data[end+1:]
    data = new

print(*data[1:])