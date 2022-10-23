# 아이디어 : topping 리스트의 길이만큼 for문을 돌면서
#           set의 원소 개수가 같은 경우가 있는지 check
# 알고리즘 : 브루트 포스, O(n^2) -> 실패
#           
# 자료구조 : set 

from collections import Counter

def solution(topping):
    answer = 0
    
    set1 = set(topping)
    set2 = set()
    counter = Counter(topping)
    
    for i in range(len(topping)) :
        counter[topping[i]] -= 1
        if counter[topping[i]] == 0 :
            set1.remove(topping[i])
    
        set2.add(topping[i])
        
        if len(set1) == len(set2) :
            answer += 1
            
    return answer