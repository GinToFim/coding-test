import re
from collections import Counter

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = [str1[i:i+2] for i in range(len(str1)) if re.findall('[a-z]{2}', str1[i:i+2])]
    B = [str2[i:i+2] for i in range(len(str2)) if re.findall('[a-z]{2}', str2[i:i+2])]
    
    A = Counter(A)
    B = Counter(B)
    
    union = sum((A | B).values())
    intersect = sum((A & B).values())
    
    if union == 0 :
        result = 1
    else :
        result = intersect / union
    
    return int(result * 65536)