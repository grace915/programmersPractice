# 백트래킹 : 현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘
# 상태공간트리를 쭉 짜는거
import itertools

# boj 15649 N과 M (n = 4, m = 3)

n, m = map(int, input().split())

stack = [-1] * m # 정담
visited = [False] * 10 # 사용했는지

def solution(k): # k는 위치
    if k == m: # 끝나면
        print(*stack)
        return
    for i in range(1, n + 1): # 1부터 n까지
        if not visited[i]: # 아직 사용하지 않은 수
            # print(k)
            stack[k] = i # 해당 위치에 i를 넣는다
            visited[i] = True  # i는 사용했다
            solution(k + 1) # 함수 호출
            visited[i] = False # 돌아오면 원래대로로
solution(0)