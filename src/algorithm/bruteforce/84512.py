from collections import deque
import sys

answer = 0


def solution(word):
    global answer

    dfs(0, "", word)

    return answer


cnt = 0


def dfs(depth, now, word):
    global answer, cnt
    if now == word:
        answer = cnt
        return
    if depth == 5:
        return

    array = ['A', 'E', 'I', 'O', 'U']
    for i in array:
        cnt += 1
        dfs(depth + 1, now + i, word)

