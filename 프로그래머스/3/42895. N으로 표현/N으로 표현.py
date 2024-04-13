# 아이디어: 1. dp 테이블에 데이터 자체가 들어감
#          2. [nn, n * n, n + n, n // n] 
# 알고리즘: dp

def solution(N, number):
    # 부분 집합들의 리스트
    set_list = list()
    
    for cnt in range(1, 8 + 1):
        # 부분 집합 선언
        sub_set = set()
        
        sub_set.add(int(str(N) * cnt))
        
        for i in range(cnt-1):
            for op1 in set_list[i]:
                for op2 in set_list[-1-i]:
                    sub_set.add(op1 * op2)
                    sub_set.add(op1 + op2)
                    sub_set.add(op1 - op2)
                    if op2 != 0:
                        sub_set.add(op1 // op2)
                    
        # number가 부분집합에 있다면
        if number in sub_set:
            return cnt
        
        # 없다면 부분집합을 리스트에 추가
        set_list.append(sub_set)
        
    # 8을 넘어가면
    return -1