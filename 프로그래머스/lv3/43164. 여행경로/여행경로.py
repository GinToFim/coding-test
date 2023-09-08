from collections import defaultdict

def solution(tickets):
    src_dict = defaultdict(list)
    
    # src-dst를 key-[value]로 하는 dictionary
    for ticket in tickets :
        src, dst = ticket
        src_dict[src].append(dst)
        
    # dict의 list들 내림차순 정렬
    for src in src_dict:
        src_dict[src].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    
    # stack이 빌 때까지
    while stack:
        top = stack[-1]
        
        # top을 출발지로 하는 것이 없거나 출발지가 다 비었을 때
        if not src_dict[top] or len(src_dict[top]) == 0 :
            path.append(stack.pop())
        else :
            stack.append(src_dict[top].pop())
    
    return path[::-1]