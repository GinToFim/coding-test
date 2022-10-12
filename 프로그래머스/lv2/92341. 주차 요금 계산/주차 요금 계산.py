# 아이디어 : 
# for record in records
# record = 시각, 차량번호, 내역
# if IN + 차량번호 not in dict
# key- 차랑번호 value - 0 가격 추가 + 스택에 차량번호 시간 추가

# if IN + 차량번호 in dict
# 가격 추가

# 알고리즘 : 구현
# 자료구조 : 출력때문에 단순 리스트 사용(index 메소드 사용) + 스택 사용

import math

def solution(fees, records):
    answer = []
    
    # 기본(단위) 시간(요금)을 분배
    default_time = fees[0]
    default_price = fees[1]
    per_time = fees[2]
    per_price = fees[3]
    
    # True False로 구분
    parking_car = dict() # 현재 주차된 상태의 차를 dictionary에 저장
    park_time = dict() # 주차된 차의 시각을 저장 
    total_time = dict() # 주차된 차량의 총 시간을 저장 
    
    for record in records :
        time, num, how = record.split()
        time = int(time[:2]) * 60 + int(time[-2:])
        
        if how == 'IN' :
            parking_car[num] = True
            park_time[num] = time
        else :
            parking_car[num] = False
            if num not in total_time :
                total_time[num] = time - park_time[num]
            else :
                total_time[num] += time - park_time[num]
                
    
    for num in parking_car.keys() :
        if parking_car[num] :
            parking_car[num] = False
            if num not in total_time :
                total_time[num] = 23*60 + 59 - park_time[num]
            else :
                total_time[num] += 23*60 + 59 - park_time[num]
    
    result = dict()
    
    for num in sorted(total_time.keys()) :
        time = total_time[num]
        total_price = default_price
        plus_time = time - default_time
        if plus_time > 0 :
            total_price += math.ceil(plus_time/per_time) * per_price
        answer.append(total_price)
    
    return answer