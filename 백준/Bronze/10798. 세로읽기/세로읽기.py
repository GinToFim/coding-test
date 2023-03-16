# 아이디어 : 1. 각 줄의 단어의 길이를 담은 length 리스트 생성
#          2. 각 줄을 출력할 때 length를 체크함
# 알고리즘

import sys
input = sys.stdin.readline

length = []
words = []

for _ in range(5) :
    word = input().rstrip()
    words.append(word)
    length.append(len(word))
    
result = ''

# length의 최대 길이일 때까지 체크
for i in range(max(length)) :
    for j in range(5) :
        # 해당 글자의 길이를 초과하였으면 무시
        if length[j] < i + 1 :
            continue
            
        result += words[j][i]

print(result)