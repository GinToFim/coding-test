def solution(babbling):
    answer = 0
    
    # 발음할 수 있는 리스트
    speak = ['aya', 'ye', 'woo', 'ma']
    
    for word in babbling:
        for s in speak:
            # 두 번 연속 발음할 수 있는 단어가 없다면
            if s * 2 not in word:
                # 발음할 수 있는 단어가 있다면 word를 공백으로 대체
                # 없다면 아무 일도 일어나지 않음
                word = word.replace(s, ' ')
        
        # 공백을 제거한 문자의 길이가 0이라면
        if len(word.strip()) == 0:
            answer += 1
    
    
    return answer