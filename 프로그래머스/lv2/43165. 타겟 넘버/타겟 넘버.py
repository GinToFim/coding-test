# 아이디어 : 
# 알고리즘 : dfs
# 자료구조 : stack(recursion)

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(depth, hap):
        nonlocal answer
        
        # 종료조건
        if depth == n:
            if hap == target :
                answer += 1
            
            return 
        
        dfs(depth + 1, hap + numbers[depth])
        dfs(depth + 1, hap - numbers[depth])
        
    dfs(0, 0)
    
    return answer