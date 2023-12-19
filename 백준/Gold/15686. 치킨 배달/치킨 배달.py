# 아이디어 : 1. 각 집(1)의 위치와 치킨집(2)의 위치를 저장하기
#          2. combinations 를 활용하여 m개만큼의 치킨집 경우의 구하기
#          2. 각 집마다 치킨집에 해당하는 최소 거리 저장하기
#          3. 치킨집을 오름차순 정렬한 뒤 M개 만큼 찾기
# 알고리즘 : 2N^3 = 2500 * 100 = 250,000 
#             250,000 * 13 = 3,250,000??
# 자료구조

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = []

for _ in range(n) :
    data.append(list(map(int, input().split())))

houses = [] # 집의 위치
chickens = [] # 치킨집의 위치

for x in range(n) :
    for y in range(n) :
        if data[x][y] == 1 :
            houses.append([x, y])
        
        if data[x][y] == 2 :
            chickens.append([x, y])

result = 10 ** 9

for case_chickens in combinations(chickens, m) :  
    # 치킨집의 최소 거리 구하기
    chicken_distances = []

    for house in houses :
        dist = []
        for chicken in case_chickens :
            hx, hy = house
            cx, cy = chicken
            
            dist.append(abs(hx-cx) + abs(hy-cy))
        
        chicken_distances.append(min(dist))
    
    result = min(sum(chicken_distances), result)
    
print(result)