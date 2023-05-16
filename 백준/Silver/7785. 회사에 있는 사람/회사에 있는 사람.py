# 아이디어 : 1. enter이면 +1, leave이면 -1
# 자료구조 : defaultdict

from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
company = defaultdict(int)

for _ in range(n) :
    name, record = input().split()
    
    if record == "enter" :
        company[name] += 1
    else :
        company[name] -= 1
    
in_company = [name for name, cnt in company.items() 
              if cnt > 0]

in_company.sort(reverse=True)

for name in in_company :
    print(name)