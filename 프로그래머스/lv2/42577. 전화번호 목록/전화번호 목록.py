# 아이디어 : 1. 오름차순 정렬
#           2. 접두사 단방향으로 탐색
# 알고리즘 : sorting (O(nlogn)) 

def solution(phone_book):
    # 오름차순 정렬
    phone_book.sort()
    
    for i in range(len(phone_book) - 1) :
        # 이전 단어가 다음 단어의 접두사라면
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    return True