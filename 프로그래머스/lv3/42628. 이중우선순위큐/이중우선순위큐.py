# 아이디어 : 1. hq 리스트 선언
#           2. 삽입의 경우 heappush 사용
#           3. 최댓값을 삭제할 경우, hq의 원소를 모두 음수를 붙인 뒤에 빼고 
#              다시 음수를 붙여서 원래대로 돌리기
#           4. 최솟값 삭제는 그냥 heappop 사용
# 알고리즘 : priorityQ -> heap
# 자료구조 : heapq

import heapq

def solution(operations):
    answer = []
    hq = []
    
    for operation in operations :
        op, num = operation.split()
        num = int(num)
        
        if op == "I" :
            heapq.heappush(hq, num)
        else :
            # 만약에 원소가 비어있다면 무시
            if len(hq) <= 0 :
                continue
            
            # 최소힙 삭제
            if num == -1 :
                heapq.heappop(hq)
            # 최대힙 삭제
            else :
                # 최대힙으로 변경
                hq = [-h for h in hq]
                heapq.heapify(hq)
                heapq.heappop(hq)
                
                # 다시 최소힙으로 변경
                hq = [-h for h in hq]
                heapq.heapify(hq)
                
    if len(hq) <= 0 :
        return [0, 0]
    else :
        return [max(hq), min(hq)]