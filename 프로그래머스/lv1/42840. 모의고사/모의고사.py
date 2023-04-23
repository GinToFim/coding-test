# 아이디어 : 1번 수포자 1 2 3 4 5
#           2번 수포자 2 1 2 3 2 4 2 5 
#           3번 수포자 3 3 1 1 2 2 4 4 5 5
# 알고리즘 : brute force (O(n) = 10,000)

def getRightCnt(supo, answers, n) :
    # 몇 배 늘리기(+1)
    times = n // len(supo) + 1
    supo = supo * times
    
    cnt = 0
    for s, a in zip(supo, answers) :
        if s == a :
            cnt += 1
    
    return cnt

def solution(answers):
    result = []
    n = len(answers)
    
    # 수포자들의 찍는 방식
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1 = getRightCnt(supo1, answers, n)
    cnt2 = getRightCnt(supo2, answers, n)
    cnt3 = getRightCnt(supo3, answers, n)
    
    cnts = [cnt1, cnt2, cnt3]
    max_cnt = max(cnts)
    
    for i in range(len(cnts)) :
        if max_cnt == cnts[i] :
            result.append(i + 1)

    return result