# 아이디어: 1. 무조건 먼 곳에서부터 배달 or 수거하기 (거리 * 2)
#          2. 택배 or 수거하는 것 둘 중에 하나라도 cap을 넘어간다면 물류창고에 갔다와야 함
# 알고리즘: 그리디

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 택배, 수거에 해당하는 양
    d_val, p_val = 0, 0
    
    # 거꾸로 탐색(가장 먼 곳 부터)
    for i in range(n-1, -1, -1):
        # 각 위치에 택배, 수거해야 하는 양 추가
        d_val += deliveries[i]
        p_val += pickups[i]
        
        # 둘 중에 하나라도 양수라면 cap에 해당하는 만큼 빼기
        # 현재 거리 만큼 물류창고 왕복
        while d_val > 0 or p_val > 0:
            d_val -= cap
            p_val -= cap
            answer += (i + 1) * 2
    
    return answer