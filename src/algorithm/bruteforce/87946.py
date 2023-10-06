n, m = 0, 0
array = []
max_ = 0
visited = []


def solution(k, dungeons):
    global n, m, now, max_, visited
    # 최대한 많이 탐험
    # 현재 피로도 k
    # 던전별 최소, 소모 피로도 dungeons

    answer = -1
    n = len(dungeons)
    m = len(dungeons[0])

    visited = [False for _ in range(n)]
    dfs(k, 0, dungeons)
    answer = max_
    return answer


temp = []


def dfs(now, cnt, dungeons):
    global n, m, array, temp, max_, visited
    # print(depth, now, cnt)
    max_ = max(max_, cnt)

    for i in range(n):
        if not visited[i]:
            a, b = dungeons[i]
            if now >= a:
                visited[i] = True
                dfs(now - b, cnt + 1, dungeons)
                visited[i] = False

