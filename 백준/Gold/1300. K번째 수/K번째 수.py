# 아이디어 : 어느 숫자가 k번째 일까?
#           특정 숫자 S보다 작거나 같은 숫자는 몇 개일까? 
#           (특정 숫자 S가 최소인가? )

#           1. K번째 숫자는 절대 K보다 클 수 없음 (end = k)
# 알고리즘 : 이진 탐색, 파라메트릭 서치

n = int(input())
k = int(input())

start, end = 1, k
result = 0

while start <= end :
    mid = (start + end) // 2
    
    cnt = 0 # mid(S)보다 적거나 같은 개수
    for i in range(1, n + 1) :
        cnt += min(n, mid // i)
    
    # 적거나 같은 개수가 충분하다면
    if cnt >= k :
        result = mid
        end = mid - 1
    else :
        start = mid + 1

print(result)