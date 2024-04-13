# 아이디어: sum hash 활용
# 알고리즘: hash -> O(N)

def solution(participant, completion):
    hash_dict = dict()
    sum_value = 0
    
    for p in participant:
        hash_dict[hash(p)] = p
        sum_value += hash(p)
    
    for c in completion:
        sum_value -= hash(c)
    
    return hash_dict[sum_value]