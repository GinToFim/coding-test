from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
foods = []

for _ in range(n) :
    foods.append(tuple(map(int, input().split())))
    
result = 10 ** 9

for i in range(1, n + 1) :
    for foods_case in combinations(foods, i) :
        sour = 1
        bitter = 0
        
        for food in foods_case :
            s, b = food
            sour *= s
            bitter += b
        
        result = min(result, abs(sour-bitter))

print(result)