# 아이디어 : 1. nCn/2로 스타트 팀과 링크 팀으로 나누기
#           2. 각각 팀의 능력치의 합들의 차를 구하기
# 알고리즘 : 20C10 = 184756

from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
data = []

all_team = [x for x in range(1, n + 1)]
result = 10 ** 9

for _ in range(n) :
    data.append(list(map(int, input().split())))

for start_team in combinations(all_team, n//2) :    
    link_team = tuple(set(all_team) - set(start_team))
    
    start_stat = 0
    for teams in combinations(start_team, 2) :
        i, j = teams
        i -= 1
        j -= 1
        
        start_stat += data[i][j]
        start_stat += data[j][i]
            
    link_stat = 0
    for teams in combinations(link_team, 2) :
        i, j = teams
        i -= 1
        j -= 1
        
        link_stat += data[i][j]
        link_stat += data[j][i]

    result = min(result, abs(start_stat-link_stat))
    
print(result)