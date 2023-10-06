from collections import deque


def solution(begin, target, words):
    answer = 0
    words.append(begin)
    n = len(words)
    visited = [0] * len(words)
    # print(words)
    # graph 만들기
    graph = [[] for i in range(n)]
    for i in range(len(words)):
        word = words[i]  # 기준 단어
        for j in range(len(words)):
            compared = words[j]  # 비교할 단어
            cnt = 0
            for c_idx in range(len(word)):
                if word[c_idx] != compared[c_idx]:
                    cnt += 1
            if cnt == 1:  # 한 글자만 다르면 변환 가능이므로 간선 정보 추가
                graph[i].append(j)
    # bfs 구하기
    q = deque([len(words) - 1])
    visited[len(words) - 1] = 1  # 시작 노드 오면 안되니까
    # print(graph)
    while q:
        now = q.popleft()

        # target이라면
        if words[now] == target:
            answer = visited[now] - 1
            break

        for num in graph[now]:
            if visited[num] == 0:
                visited[num] = visited[now] + 1
                q.append(num)

    return answer