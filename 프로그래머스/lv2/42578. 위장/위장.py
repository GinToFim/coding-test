from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)
    
    for name, kind in clothes :
        clothes_dict[kind].append(name)
        
    for kind in clothes_dict :
        answer *= len(clothes_dict[kind]) + 1
        print(answer)
    
    # 모두 벗은 경우 제외
    return answer - 1