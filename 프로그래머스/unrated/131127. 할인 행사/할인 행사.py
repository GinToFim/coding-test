def solution(want, number, discount):
    answer = 0
    while len(discount) >= 10:
        days = discount[:10]
        for item, n in zip(want, number):
            if days.count(item) !=n:
                break
            if item == want[-1]:
                answer += 1
        discount.pop(0)
        
    return answer