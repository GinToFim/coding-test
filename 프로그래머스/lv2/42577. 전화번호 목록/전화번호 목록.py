def solution(phone_book):
    # hash 테이블 생성
    hash_map = dict()
    
    # phone_book에 들어있는 모든 요소 담기
    for phone_num in phone_book :
        hash_map[phone_num] = 1
    
    # 접두어 찾기
    for phone_num in phone_book :
        prefix = ''
        for num in phone_num :
            prefix += num
            # 접두어가 hash_map에 존재하는데, 접두어와 기존 번호와 같을 경우는 제외
            if prefix in hash_map and prefix != phone_num :
                return False
    
    return True