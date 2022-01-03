def solution(clothes):
    from collections import Counter
    from functools import reduce

    # (name, kind) in clothes 그중 kind의  개수
    cnt = Counter([kind for name, kind in clothes])
    print(cnt)
    # 의상종류
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) -1
    return answer

clothes = [["1", "face"], ["2", "face"], ["3", "top"], ["4", "pants"], ["5", "outer"]]
print(solution(clothes))

# reduce(집계함수, 순회가능한데이터[,초기값])