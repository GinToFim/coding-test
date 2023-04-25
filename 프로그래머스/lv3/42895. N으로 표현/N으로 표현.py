# 아이디어
# 알고리즘 : Dynamic Programming

def solution(N, number):
    set_list = []
    
    for cnt in range(1, 8 + 1) :
        partial_set = set()
        partial_set.add(int(str(N) * cnt))
        
        for i in range(cnt - 1) :
            for op1 in set_list[i] :
                for op2 in set_list[-1-i] :
                    partial_set.add(op1 * op2)
                    partial_set.add(op1 + op2)
                    partial_set.add(op1 - op2)
                    if op2 != 0 :
                        partial_set.add(op1 // op2)
        
        # 원하는 숫자가 그룹 안에 있담녀
        if number in partial_set :
            return cnt
        
        # 없으면 부분 집합은 리스트에 추가
        set_list.append(partial_set)
        
    # 8을 넘어가면       
    return -1