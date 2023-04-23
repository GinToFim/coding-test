from itertools import combinations

n, m = map(int, input().split())

for iters in combinations(range(1, n + 1), m) :
    print(*iters)