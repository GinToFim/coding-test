# 아이디어 : 가장 가치가 큰 동전부터 나누기 
# 알고리즘 : 그리디

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin_types = [int(input().rstrip()) for _ in range(n)]
result = 0 

for coin in coin_types[::-1] :
    result += k // coin
    k %= coin
    
print(result)