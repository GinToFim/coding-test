def solution(slice, n):
    cnt = 1
    while cnt * slice < n :
        cnt += 1
    
    return cnt