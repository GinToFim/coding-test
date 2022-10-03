def solution(n, words):
    answer = []
    turn = 0
    wordList = [words[0]]

    for idx in range(1, len(words)):
        if words[idx-1][-1] != words[idx][0]:
            turn = idx
            break
        if words[idx] in wordList:
            turn = idx
            break
        wordList.append(words[idx])
    answer = [turn%n +1, turn//n + 1]
    if turn == 0:
        answer = [0, 0]
    return answer