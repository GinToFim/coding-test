# 아이디어: 
# 알고리즘: 구현, 문자열

def solution(babbling):
    answer = 0
    
    yes_bab = ['aya', 'ye', 'woo', 'ma']
    no_bab = [y*2 for y in yes_bab]

    
    for word in babbling:
        # 단어가 없어질 때까지
        while word:
            # 앞 두 글자가 가능하면서 앞 네 글자가 연속이지 않다면
            if word[:2] in yes_bab and word[:4] not in no_bab:
                # 두 글자 줄이기
                word = word[2:]
            # 앞 두 글자가 가능하면서 앞 네 글자가 연속이지 않다면    
            elif word[:3] in yes_bab and word[:6] not in no_bab:
                # 세 글자 줄이기
                word = word[3:]
            else:
                break
    
        # 글자가 남아있지 않다면
        if not word:
            answer += 1
    
    return answer