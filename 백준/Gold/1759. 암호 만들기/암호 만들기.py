from itertools import combinations
import sys

input = sys.stdin.readline

l, c = map(int, input().split())
string = input().split()

# 오름차순 배열
string.sort()

for string_case in combinations(string, l) : 
    v_cnt = 0 # 모음 개수
    c_cnt = 0 # 자음 개수
    
    for ch in string_case :
        if ch not in 'aeiou' :
            c_cnt += 1
        if ch in 'aeiou' :
            v_cnt += 1
        
    if v_cnt < 1 or c_cnt < 2 :
        continue
        
    print(''.join(string_case))