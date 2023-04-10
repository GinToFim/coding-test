def solution(s):
    result = []
    chars = dict()
    
    for ch in s :
        if ch in chars.keys() :
            result.append(chars[ch])
            chars[ch] = 0
        else :
            result.append(-1)
            chars[ch] = 0
        
        for key in chars.keys() :
            chars[key] += 1
    
    return result