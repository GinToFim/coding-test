import math
from collections import defaultdict

def get_fee(minutes, fees) :
    # default, per
    dm, dp, pm, pp = fees
    return dp + math.ceil(max(0, minutes-dm) / pm) * pp

def solution(fees, records): 
    parking = {} # 현재 주차중인 차를 기록하는 딕셔너리
    park_time = defaultdict(int) # 차가 주차된 시간을 기록하는 딕셔너리
    
    for record in records :
        _time, car, cmd = record.split()
        hour, minute = _time.split(':')
        minutes = int(hour) * 60 + int(minute)
        
        if cmd == 'IN' :
            parking[car] = minutes
        else :
            park_time[car] += minutes - parking[car]
            del parking[car]
    
    # 남아있는 차를 23:59으로 빼기
    for car in parking.keys() :
        park_time[car] += 23*60 + 59 - parking[car]
    
    return [get_fee(park_time[car], fees) for car in sorted(park_time.keys())]