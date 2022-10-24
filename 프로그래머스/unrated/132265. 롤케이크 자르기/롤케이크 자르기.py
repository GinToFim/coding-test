# 아이디어 : 매번 set를 초기화하지말고
#           add, remove로 원소를 추가/제거하기
# 알고리즘
# 자료구조

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