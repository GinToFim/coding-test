# 아이디어 : 도착지를 기준으로 오름차순 정렬
# 알고리즘 : 정렬, 그리디

def solution(routes):
    answer = 0
    
    # 오름차순 정렬
    routes.sort(key=lambda x : x[1])
    camera = -30001 # 진입 지점 보다 뒤로 초기화
    
    for start, end in routes :
        # 설치된 카메라보다 차량의 진입 지점이 앞에 있다면
        if start > camera:
            answer += 1
            camera = end # 그 차랑의 도착 지점에 카메라 설치  
    
    return answer