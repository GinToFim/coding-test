# 아이디어 : 이 정도 시간이 주어지면 충분한가? yes or no?
# 알고리즘 : binary search(O(logn) = 10 * 10 * 10 = 10^3)
#           parametric search

def solution(n, times):
    answer = 0
    
    start, end = 0, max(times) * n
    
    while start <= end :
        mid = (start + end) // 2
        total = 0 # 통과된 사람 수
        
        for time in times :
            total += mid // time

        # 충분하다면(-> 상한선 줄이기)
        if total >= n :
            answer = mid
            end = mid - 1
        else :
            start = mid + 1
    
    return answer