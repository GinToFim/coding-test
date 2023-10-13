# 아이디어: 1. terms를 dict로 바꾸기(month 기준)
#          2. privacy가 today보다 작으면 result에 추가
#          3. today_yyyy > p_y
# 알고리즘: 구현

def solution(today, terms, privacies):
    answer = []
    
    # 약관 종류 dict 생성
    terms = {t[0]: int(t[2:]) for t in terms}
    
    today = today.split('.')
    today = int(''.join(today))
    
    for idx, privacy in enumerate(privacies):
        privacy, ch = privacy.split()
        
        p_year = int(privacy[:4])
        p_month = int(privacy[5:7]) + terms[ch]
        p_day = int(privacy[8:]) - 1
        
        while p_month > 12:
            p_month -= 12
            p_year += 1
        
        if p_day == 0:
            p_day = 28
            p_month -= 1
            if p_month == 0:
                p_month = 12
                p_year -= 1
            
            
        privacy_day = p_year * 10000
        privacy_day += p_month * 100
        privacy_day += p_day
        
        if today > privacy_day:
            answer.append(idx+1)
        
        print(today, privacy_day)

    
    return answer