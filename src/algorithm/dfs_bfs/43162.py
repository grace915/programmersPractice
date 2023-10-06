from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    dq = deque()

    def bfs(start):
        dq.append(start)
        while dq:
            now = dq.popleft()
            if visited[now] == 0:  # 이 점에 방문했는지
                visited[now] = 1  # 이 점에 방문했는지
            for i in range(len(computers)):  # 가진 목록만큼
                if computers[now][i] == 1 and visited[i] == 0:  # 해당 점이랑 연결되고, 그 점에 방문안했으면
                    dq.append(i)

    while 0 in visited:
        answer += 1
        bfs(visited.index(0))
    return answer