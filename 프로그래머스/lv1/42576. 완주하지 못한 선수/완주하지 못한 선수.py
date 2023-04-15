# SUM hash
# hash 함수를 이용하여 sum_hash로 participant를 모두 더하고
# completion를 모두 빼고 남은 값이 정답

def solution(participant, completion):
    sum_hash = 0
    hash_dict = dict()
    
    for part in participant :
        hash_dict[hash(part)] = part
        sum_hash += hash(part)
        
    for com in completion :
        sum_hash -= hash(com)
    
    return hash_dict[sum_hash]