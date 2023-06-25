# 아이디어 : 1. 오름차순 정렬
#           2. 
# 알고리즘 : sorting, two pointer, brute force
#           2,000 * 2,000 = 4,000,000

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort() # 오름차순

result = 0 # 좋은 수 개수


# 배열에서 하나씩 확인
for i in range(n) :
    tmp = data[:i] + data[i+1:]
    target = data[i]
    
    start, end = 0, n-2
    
    # 좋은 수 인지 확인
    while start < end :
        hap = tmp[start] + tmp[end]
        
        if hap == target :
            result += 1
            break
        elif hap < target :
            start += 1
        else :
            end -= 1

print(result)