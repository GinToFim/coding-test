# 아이디어 : 1. parent dict 만들기 + result table 비용 만들기
#           2. 
# 알고리즘 : 
# 자료구조 : dict


def solution(enroll, referral, seller, amount):
    result = {en : 0 for en in enroll}
    result['center'] = 0
    parent_dict = dict()
    for en, re in zip(enroll, referral) :
        if re == '-' :
            parent_dict[en] = 'center'
        else :
            parent_dict[en] = re
    
    for se, am in zip(seller, amount) :
        cost = am * 100
        if cost == 0 :
            continue
        parent = parent_dict[se] 
        child = se

        parent_cost = int(cost * 0.1)
        child_cost = cost - parent_cost

        result[parent] += parent_cost
        result[child] += child_cost

        while True : 
            se = parent
            if se == 'center' :
                break
            cost = parent_cost
            result[parent] -= cost
            if cost == 0 :
                break
            
            parent = parent_dict[se] 
            child = se

            parent_cost = int(cost * 0.1)
            child_cost = cost - parent_cost

            result[parent] += parent_cost
            result[child] += child_cost

    return list(result.values())[:-1]