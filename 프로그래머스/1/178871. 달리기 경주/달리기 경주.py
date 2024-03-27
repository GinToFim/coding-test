# 아이디어:
# 알고리즘:
# 자료구조: dict

def solution(players, callings):
    str_ranking = {player: idx for idx, player in enumerate(players)}
    num_ranking = {idx: player for idx, player in enumerate(players)}

    for calling in callings:
        slow_rank = str_ranking[calling]
        fast_rank = slow_rank - 1

        fast_player = num_ranking[slow_rank]
        slow_player = num_ranking[fast_rank]

        str_ranking[fast_player] = fast_rank
        str_ranking[slow_player] = slow_rank
        num_ranking[fast_rank] = fast_player
        num_ranking[slow_rank] = slow_player
    
    answer = [num_ranking[rank] for rank in range(len(players))]
    return answer