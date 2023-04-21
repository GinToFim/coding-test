def solution(s, skip, index):
    answer = ''
    alphabet = ''
    for ch in range(ord('a'), ord('z') + 1) :
        alphabet += chr(ch)
    
    # 암호 사전
    alpha_dict = dict()
    key = 0
    for ch in alphabet :
        if ch in skip :
            continue
        
        alpha_dict[key] = ch
        alpha_dict[ch] = key
        key += 1
    
    length = key
    for ch in s :
        num = alpha_dict[ch]
        key = (num + index) % length
        answer += alpha_dict[key]
    
    return answer