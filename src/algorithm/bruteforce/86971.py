from collections import deque

import sys

sys.setrecursionlimit()
def bfs(flag, tree):
    queue = deque()
    queue.append(flag)


    visited = []
    answer = 1
    while queue:
        x = queue.popleft()
        for i in range(len(tree[x])):
            if tree[x][i] != 0 and i not in visited:
                visited.append(x)
                queue.append(i)
                answer += 1

    return answer


def solution(n, wires):
    answer = 101
    delete = 0
    for i in range(len(wires)):
        tree = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(len(wires)):
            if j != delete:
                tree[wires[j][0]][wires[j][1]] = 1
                tree[wires[j][1]][wires[j][0]] = 1
        a = bfs(wires[delete][0], tree)
        b = n - a
        delete += 1
        answer = min(answer, (abs(a - b)))

    return answer