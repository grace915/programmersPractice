from collections import deque


def solution(maps):
    answer = []

    q = deque()
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]

    n = len(maps)
    m = len(maps[0])

    q.append([0, 0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = True
                q.append([nx, ny])

    if maps[-1][-1] == 1:
        return -1
    answer = maps[-1][-1]
    return answer
