from itertools import permutations

n, m = map(int, input().split())

for iters in permutations(range(1, n + 1), m) :
    print(*iters)