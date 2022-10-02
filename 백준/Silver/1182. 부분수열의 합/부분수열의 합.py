from itertools import combinations 
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
result = 0

for x in range(1, n + 1) :
	for sub_data in combinations(data, x) :
		if sum(sub_data) == s :
			result += 1

print(result)