# 아이디어 : hash
# 알고리즘 : hash 
# 자료구조 : dictionary

def solution(participant, completion):
    hash_dict = dict()
    sum_hash = 0
    
    for p in participant :
        sum_hash += hash(p)
        hash_dict[hash(p)] = p
        
    for c in completion :
        sum_hash -= hash(c)
    
    return hash_dict[sum_hash]