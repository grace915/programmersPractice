def solution(sizes):
    w = 0
    h = 0
    for size_set in sizes:
        size_set.sort()
        if size_set[0] > w:
            w = size_set[0]
        if size_set[1] > h:
            h = size_set[1]

    answer = w * h
    return answer



def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col