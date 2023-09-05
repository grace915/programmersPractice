def solution(participant, completion):
    # result = ""

    dic = {}
    for p in participant:
        if p in dic:
            dic[p] = dic[p] + 1
        else:
            dic[p] = 1

    for c in completion:
        dic[c] = dic[c] - 1

    reverse_dic = dict(map(reversed, dic.items()))
    answer = reverse_dic[1]

    # answer = result
    return answer
# 다른사람의 풀이



def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]