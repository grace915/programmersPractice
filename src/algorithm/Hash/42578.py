def mul(x, y):
    return x * y


def solution(clothes):
    answer = 1
    h = {}
    for i, j in clothes:
        if j in h:
            h[j] += 1
        else:
            h[j] = 2

    for v in h.values():
        answer *= v
    print(answer)
    return answer - 1
