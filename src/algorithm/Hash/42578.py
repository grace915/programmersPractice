def solution(clothes):
    answer = 1

    h = {}
    for i, j in clothes:
        if j in h:
            h[j] += 1
        else:
            h[j] = 1

    for v in h.values():
        print(v + 1)
        answer *= (v + 1)

    answer -= 1
    return answer