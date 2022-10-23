def solution(rsp):
    answer = ''
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    
    for ch in rsp :
        answer += rsp_dict[ch]
    
    return answer