import collections


def solution(numbers, target):
    total = 0

    def dfs(index, total):
        if len(numbers) == index:
            if total == target:
                return 1
            return 0

        ret = 0
        ret += dfs(index + 1, total + numbers[index]) # 더하거나
        ret += dfs(index + 1, total - numbers[index]) # 빼거나
        return ret

    return dfs(0, 0)