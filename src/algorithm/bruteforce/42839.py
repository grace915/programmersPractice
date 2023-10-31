import itertools


def solution(numbers):
    answer = set()
    array = []

    for i in range(1, len(numbers) + 1):
        array += list(itertools.permutations(numbers, i))

    # case 숫자로 만들기

    answer = set(int(''.join([str(t) for t in temp])) for temp in array)
    answer -= set(range(0, 2))
    for i in range(2, int(max(answer) ** 0.5) + 1):
        answer -= set(range(i * 2, max(answer) + 1, i))
        # 젤 큰 수의 제곱근까지의 모든 수의 배수를 뺀다..!

    return len(answer)
