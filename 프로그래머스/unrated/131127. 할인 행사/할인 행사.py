def solution(want, number, discount) -> int:
    today_discount = {key: discount[:10].count(key) for key in set(discount[:10])}
    answer = 0
    for i in range(len(discount) - 10 + 1):
        for key, value in zip(want, number):
            if today_discount.get(key, 0) < value:
                break
        else:
            answer += 1
        # sliding_window기법을 사용했지만, 사실 이번 문제에서는 안써도 비슷하다.
        # 이유: 리스트의 합이나 곱같은 문제가 아니고 리스트를 슬라이싱만 해도 해결이됨.
        if i != len(discount) - 10:
            today_discount[discount[i]] -= 1
            today_discount[discount[i + 10]] = (
                today_discount.get(discount[i + 10], 0) + 1
            )
    return answer