# 아이디어
# 알고리즘 : permutation (순열)


from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
inequals = list(input().split())

result = []

for nums in permutations(range(10), n + 1) :
    past = nums[0]
    flag = True
    
    for inequal, num in zip(inequals, nums[1:]) :
        if inequal == '<' :
            if not (past < num) :
                flag = False
                break
        else :
            if not (past > num):
                flag = False
                break
                
        past = num
        
    if flag :
        result.append(nums)

min_num = result[0]
max_num = result[-1]

min_num = [str(x) for x in min_num]
max_num = [str(x) for x in max_num]

print(''.join(max_num))
print(''.join(min_num))