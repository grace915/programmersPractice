answer = {}
visited = [False] * 7
import itertools
def solution(numbers):

    # 소수는 어떻게 만들까
    # 1이 아니고 다른 수로 나눠지는지를 봐야함
    # 2부터 자기 수 - 1로 나눴을 때 나눠지는지 안나눠지는지를 보자


    array = []
    answer = []
    for i in range(1, len(numbers) + 1):
        array += list(itertools.permutations(numbers, i))


    # case 숫자로 만들기
    cases = list(set(int(''.join([str(t) for t in temp] )) for temp in array))

    for case in cases:
        if case == 1 or case == 0:
            continue

        check = 0

        # 소수인지 아닌지
        for i in range(2, case):
            if case % i == 0:
                check += 1
        if check == 0:
            answer.append(case)

    print(len(answer))

solution("011")