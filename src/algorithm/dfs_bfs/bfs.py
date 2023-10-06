
array = []
q = []
visited = []
def bfs():
    q.append(0) # 시작점
    visited[0] = True

    # 연결된게 없어질때까지
    while not q:
        now = q[0] # 젤 앞쪽 친구부터 사용하기
        print(now)

        for i in range(len(array[now])):
            if not visited[array[now][i]]: # 방문 안했으면
                q.append(array[now][i]) # 큐에 그 정점 push
                visited[array[now][i]] = True
