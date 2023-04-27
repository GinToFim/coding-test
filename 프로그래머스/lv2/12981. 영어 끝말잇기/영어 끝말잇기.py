# 아이디어 : 1. 지금까지 나왔던 단어들은 set에 추가
#           2. 현재 끝말잇기 순서를 세기 (cnt = 0 부터 시작)
#           3. 이전 단어의 맨 뒤와 현재 단어 앞이 다르다면 return
#           4. 끝까지 가면 [0, 0]


# [번호, 차례] return
# 알고리즘 : 구현

def solution(n, words):
    answer = []
    word_set = set()
    cnt = 0 # 끝말잇기 개수
    
    past_word = words[0]
    word_set.add(words[0])
    cnt += 1
    
    for word in words[1:] :
        # 만약 말했던 단어 이거나 끝말잇기가 불가능하다면
        if word in word_set or past_word[-1] != word[0] :
            return [cnt%n + 1, cnt//n+1]
        
        # 가능하다면
        past_word = word
        word_set.add(word)
        
        cnt += 1
    
    # 모두 끝말잇기가 가능하다면
    return [0, 0]