# 아이디어 : 1. 100 X 100의 배열 만들기 (원소는 모두 0으로)
#          2. 해당하는 점을 1로 만들기
#          3. 해당 배열의 sum 출력

# 알고리즘 : dynamic programming

import sys
input = sys.stdin.readline

n = int(input())

canvas = [[0] * 101 for _ in range(101)]

for _ in range(n) :
    a, b = map(int, input().split())
    
    for x in range(a, a + 10) :
        for y in range(b, b + 10) :
            canvas[x][y] = 1

result = 0
for i in range(1, 101) :
    result += sum(canvas[i])

print(result)