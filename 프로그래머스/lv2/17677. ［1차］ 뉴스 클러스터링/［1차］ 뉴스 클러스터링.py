# 아이디어 
# 알고리즘
# 자료구조 : set, Counter

from collections import Counter

def solution(str1, str2):
    # 소문자화
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = []
    for i in range(len(str1)-1) :
        tmp = str1[i:i+2]
        if tmp.isalpha() :
            A.append(tmp)
        
    B = []
    for i in range(len(str2)-1) :
        tmp = str2[i:i+2]
        if tmp.isalpha() :
            B.append(tmp)

    A = Counter(A)
    B = Counter(B)
    union = sum((A | B).values())
    intersect = sum((A & B).values())
    
    if union == 0 :
        return 65536
    else :
        print(union, intersect)
        return int(intersect/union*65536)