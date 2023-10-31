def solution(name, yearning, photo):
    answer = []

    name_yearning = dict(zip(name, yearning))

    for names in photo:
        sum = 0
        for name in names:
            if name in name_yearning:
                sum += name_yearning[name]
        answer.append(sum)
    return answer