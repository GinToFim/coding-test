# 아이디어:
# 알고리즘: 브루트포스, 백트래킹

def solution(word):
    answer = 0
    
    vowels = 'AEIOU'
    word_list = []
    result = []
    
    def dfs(depth, limit):
        # 종료조건
        if depth == limit:
            word_list.append("".join(result))
            return
        
        for i in range(len(vowels)):
            result.append(vowels[i])
            dfs(depth + 1, limit)
            result.pop()

    for limit in range(1, 6):
        dfs(0, limit)
            
    # 오름차순 정렬
    word_list.sort()
    
    return word_list.index(word) + 1