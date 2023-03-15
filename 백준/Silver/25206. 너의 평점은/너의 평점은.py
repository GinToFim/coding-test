import sys
input = sys.stdin.readline

table = dict()
table["A+"] = 4.5
table["A0"] = 4.0
table["B+"] = 3.5
table["B0"] = 3.0
table["C+"] = 2.5
table["C0"] = 2.0
table["D+"] = 1.5
table["D0"] = 1.0
table["F"] = 0.0

total_score = 0
total_credit = 0

for _ in range(20) :
    _, credit, score = input().split()
    if score == "P" :
        continue
    credit = float(credit)
    score = table[score]
    
    total_score += credit * score
    total_credit += credit
    
result = total_score / total_credit
print(f"{result:0.6f}")