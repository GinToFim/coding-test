import math
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
t, p = map(int, input().split())

t_bundle = 0

for x in data:
    t_bundle += math.ceil(x / t)
print(t_bundle)

p_bundle = n // p
p_remainder = n % p
print(p_bundle, p_remainder) 