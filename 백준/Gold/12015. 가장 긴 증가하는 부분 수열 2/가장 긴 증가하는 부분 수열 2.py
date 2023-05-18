# 아이디어 : 1. result 테이블 초기화
# 알고리즘 LIS - Bianry Search

import bisect
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

result = [data[0]]

for x in data[1:] :
    # 더 크다면(증가하는 수열이 가능하다면)
    if result[-1] < x :
        result.append(x)
    # 더 작다면
    else :
        idx = bisect.bisect_left(result, x)
        result[idx] = x # 해당 인덱스 자리를 현재값으로 바꾸기
        
print(len(result))