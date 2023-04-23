# 아이디어 : 1. 모음 'A', 'E', 'I', 'O', 'U' 길이 5 이하인 리스트 만들기
#           2. 리스트 정렬 수행
# 알고리즘 : brute force, 중복 순열(백트래킹), sort
#          O(5^n) = 5^5 = 3125


def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    word_list = []
    result = []
    
    def dfs(num, limit) :
        if num == limit :
            word_list.append(''.join(result))
            return
        
        for i in range(len(vowels)) :
            result.append(vowels[i])
            dfs(num+1, limit)
            result.pop()
            
    dfs(0, 1)
    dfs(0, 2)
    dfs(0, 3)
    dfs(0, 4)
    dfs(0, 5)
    
    word_list.sort()
    
    return word_list.index(word) + 1