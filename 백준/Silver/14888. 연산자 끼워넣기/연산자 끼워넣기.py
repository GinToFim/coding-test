import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -int(1e9)
min_value = int(1e9)

def dfs(idx, num) :
	global max_value, min_value, add, sub, mul, div

	if idx == n :
		max_value = max(max_value, num)
		min_value = min(min_value, num)
		return 

	if add > 0 :
		add -= 1
		dfs(idx + 1, num + data[idx])
		add += 1
	if sub > 0 :
		sub -= 1
		dfs(idx + 1, num - data[idx])
		sub += 1
	if mul > 0 :
		mul -= 1
		dfs(idx + 1, num * data[idx])
		mul += 1
	if div > 0 :
		div -= 1
		dfs(idx + 1, int(num / data[idx]))
		div += 1

# dfs 호출
dfs(1, data[0])
		
print(max_value)
print(min_value)