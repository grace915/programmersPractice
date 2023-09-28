def solution(numbers, target):
    answer = 0

    tree = [0]
    for n in numbers:
        list = []
        for i in tree:
            list.append(i - n)
            list.append(i + n)
        tree = list
    answer = tree.count(target)
    return answer