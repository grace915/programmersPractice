def solution(brown, yellow):
    answer = []
    # 가로 >= 세로
    # yellow로 할 수 있는 경우

    y = set()
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y.add((max(i, yellow // i), min(i, yellow // i)))

    for w, h in y:
        if (w + 2) * (h + 2) - yellow == brown:
            answer = [w + 2, h + 2]

    return answer