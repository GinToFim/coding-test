# 아이디어: 1. emoticons의 할인율의 경우의 수 나누기(10, 20, 30, 40)
# 알고리즘: 구현, 브루트 포스
# 100 * 4 * 7 => 1,000,000

from itertools import product

def solution(users, emoticons):
    answer = []
    n = len(emoticons) # 이모티콘 개수
    plus_cnt = 0 # 카톡 플러스 이용자 수
    total_amount = 0 # 이모티콘 판매액
    
    
    # 10, 20, 30, 40으로 수정
    for sale_case in product([10, 20, 30, 40], repeat=n):
        now_amount = 0
        now_plus = 0
        
        for user in users:
            tmp_amount = 0
            for sale, emoticon in zip(sale_case, emoticons):
                # 유저가 설정한 세일보다 크거나 같다면
                if sale >= user[0]:
                    tmp_amount += emoticon * (100 - sale) / 100
            
            # 유저가 산 이모티콘 액수가 플러스 가입 기준보다 높거나 같디면
            if tmp_amount >= user[1]:
                now_plus += 1
            else:
                now_amount += tmp_amount
        
        if plus_cnt < now_plus:
            plus_cnt = now_plus
            total_amount = now_amount
        elif plus_cnt == now_plus:
            total_amount = max(total_amount, now_amount)
    
    
    return [plus_cnt, total_amount]