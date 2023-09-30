# 정수의 개수 n, 정수 s
# n개의 정수
n, s = map(int, input().split())
l = list(map(int, input().split()))


visited = [False] * n
answer = 0
def solution(count, total):
    global answer
    if count == n:
        if total == s:
            answer += 1
        return

    # 트리 구조가 나를 넣거나 / 안넣거나
    solution(count + 1, total)
    solution(count + 1, total + l[count])

solution(0,0)
if s == 0:
    answer -= 1
print(answer)