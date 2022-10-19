# 아이디어 : 1. 단어를 저장할 딕셔너리를 생성
#           2. start와 end를 기준으로 단어를 만들어 사전에 있는지 확인
#           3. 투 포인터(start, end) 갱신
# 알고리즘 : 구현, 투 포인터

def solution(msg):
    result = []
    
    # 단어를 저장할 딕셔너리 생성
    voca = dict()
    for i in range(ord('A'), ord('Z') + 1) :
        key = chr(i)
        value = i - ord('A') + 1
        voca[key] = value
    
    # 투 포인터와 딕셔너리 최대값 변수 설정
    start, end = 0, len(msg)
    max_value = 26
    
    while True :
        word = msg[start:end]
        
        # 사전에 단어가 있다면
        if word in voca.keys() :
            result.append(voca[word])
            
            if end >= len(msg) :
                return result
            
            # 사전에 있는 단어 + 바로 뒷문자
            key = word + msg[end]
            voca[key] = max_value + 1 # 사전에 단어 추가
            max_value += 1

            # 투 포인터 초기화
            start += len(word)
            end = len(msg)
        else : # 사전에 단어가 없다면
            end -= 1 # 단어 길이 줄이기
            
            
            
    