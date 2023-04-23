from itertools import product 

n, m = map(int, input().split())

for iters in product(range(1, n + 1), repeat=m) :
    print(*iters)