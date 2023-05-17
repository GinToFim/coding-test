# 아이디어 : 1. 이 정도 시간이면 충분한가?
#           2. start : 0, end : max(times) * n
# 알고리즘 : 10^9 -> 이진 탐색, 파라메트릭 서치


def solution(n, times):
    answer = 0
    start, end = 0, max(times) * n
    
    # mid는 심사가 걸리는 시간
    while start <= end :
        mid = (start + end) // 2
        
        total = 0 # 심사한 인원 수
        
        for t in times :
            total += mid // t
        
        # 심사한 인원 수가 충분하다면, 상한선 줄이기
        if total >= n :
            answer = mid
            end = mid - 1
        else :
            start = mid + 1
    
    return answer