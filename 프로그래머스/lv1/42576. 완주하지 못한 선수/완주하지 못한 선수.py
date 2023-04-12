from collections import Counter

def solution(participant, completion):
    p_cnt = Counter(participant)
    c_cnt = Counter(completion)
    fail = (p_cnt - c_cnt).most_common()[0][0]
    
    return fail