# 아이디어 : 
# 알고리즘 : 슬라이딩 윈도우

import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())

sub_dna = dna[:p]
acgt_dict = {'A':0, 'C':0, 'G':0, 'T':0}

for ch in sub_dna :
    acgt_dict[ch] += 1
    
result = 0
if acgt_dict['A'] >= a and acgt_dict['C'] >= c and acgt_dict['G'] >= g and acgt_dict['T'] >= t :
    result += 1

for i in range(p, s):
    acgt_dict[dna[i-p]] -= 1
    acgt_dict[dna[i]] += 1
    
    if acgt_dict['A'] >= a and acgt_dict['C'] >= c and acgt_dict['G'] >= g and acgt_dict['T'] >= t :
        result += 1
    
print(result)