# 아이디어 : AGCT 알파벳들의 슬라이딩 윈도우
# 알고리즘 : 슬라이딩 윈도우

import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = input().rstrip()
a, c, g, t = map(int, input().split())

need_acgt = {'A':a, 'C':c, 'G':g, 'T':t} # 조건으로 필요로하는 acgt
now_acgt = {ch : 0 for ch in "ACGT"} # window 별 acgt

sub_dna = dna[:p]

for ch in sub_dna :
    if ch in now_acgt :
        now_acgt[ch] += 1
        
result = 0
flag = True
# 처음 sub_dna가 되는지 확인
for ch in "ACGT":
    # 조건에 만족하지 않으면
    if need_acgt[ch] > now_acgt[ch] :
        flag = False
        break
        
if flag :
    result += 1

for i in range(p, s):
    # 다음 문자가 acgt 에 들어간다면
    if dna[i] in "ACGT":
        now_acgt[dna[i]] += 1
    
    if dna[i-p] in "ACGT":
        now_acgt[dna[i-p]] -= 1
        
    flag = True
    for ch in "ACGT":
        # 조건에 만족하지 않으면
        if need_acgt[ch] > now_acgt[ch] :
            flag = False
            break

    if flag :
        result += 1
        
print(result)