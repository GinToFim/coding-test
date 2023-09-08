# 아이디어 : dfs를 활용하여 경우의 수 구하기
# 알고리즘 : dfs

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(depth, num):
        nonlocal answer
        
        # 종료 조건
        if depth == n :
            if num == target :
                answer += 1
            return
        
        # 더하기 빼기 정의
        dfs(depth + 1, num + numbers[depth])
        dfs(depth + 1, num - numbers[depth])
        
    # 함수 실행
    dfs(0, 0)
    
    return answer