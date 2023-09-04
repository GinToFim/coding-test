import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

cost = 0
for i in range(1, n) :
	cost += distance[i-1] * min(oil[:i])

print(cost)