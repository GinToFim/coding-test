def solution(phone_book):
    phone_book=sorted(phone_book) #String이므로 사전순으로 정렬된다.
    for i in range(len(phone_book)-1): #인덱스로 반복문 돌리기 맨마지막 요소는 제외 
        str = phone_book[i]
        if(str==phone_book[i+1][:len(str)]): #앞서 맨 마지막 인덱스 제외 안 하면 여기서 오류 걸림 
             return False

    return True
