# 아이디어 : 1. 연속된 부분합이 S보다 작으면 end 증가
#           2. 연속된 부분합이 s보다 크거나 같으면 start 증가
#           3. start와 end 차이는 계속 기억
# 알고리즘 : two pointers

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

start, end = 0, 0
interval_sum = 0 # 부분합
result = n + 1 # end와 start의 차이

for start in range(n):
    while interval_sum < s and end < n :
        interval_sum += data[end]
        end += 1
        
    if interval_sum >= s and (end - start) < result :
        result = end - start
    
    interval_sum -= data[start]

# 해당하는 부분합이 없다면
if result >= n + 1 :
    print(0)
else :
    print(result)