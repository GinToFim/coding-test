# 아이디어 : 
# 알고리즘 : 

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
start, end = 0, n - 1

result = abs(data[start] + data[end])
final = [data[start], data[end]]

while start < end :
    # 절댓값 합 계산
    hap = data[start] + data[end]
    
    # 갱신한 절대값이 더 작다면
    if abs(hap) < result :
        result = abs(hap)
        final = [data[start], data[end]]
        # 0 이 나왔다면 바로 종료
        if result == 0 :
            break
    
    # 합이 음수가 나왔다면
    if hap < 0 :
        start += 1
    # 합이 양수가 나왔다면
    else :
        end -= 1

print(*final)