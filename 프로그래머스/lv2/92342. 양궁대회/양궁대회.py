# 중복조합 (음이 아닌 정수해의 개수)
# 11H10 = 20C10 = 184,756 가능?

from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    mymax = 0
    for temp in list(combinations_with_replacement(range(0, 11), n)):
        ryan_now = [0 for _ in range(11)]
        for t in temp:
            ryan_now[10 - t] += 1

		# 라이언 점수랑 어피치 점수 비교함
        ryan = 0
        apeach = 0
        for i in range(11):
            r, a = ryan_now[i], info[i]

            if r == a == 0:
                continue
            if r > a:
                ryan += (10 - i)
            else:
                apeach += (10 - i)

        if ryan > apeach:
            if mymax < (ryan - apeach):
                mymax = ryan - apeach
                answer = ryan_now

    if answer == []:
        return [-1]
    
    return answer