# 아이디어:
# 알고리즘: 정렬, startswith 

def solution(phone_book):
    # 오름차순 정렬
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        # 접두어라면
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    
    return True