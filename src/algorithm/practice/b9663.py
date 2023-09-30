n = int(input())

# queen은 좌, 우, 위, 아래, 대각선 위치에 없어야 한다
# 한 행에 한 q만 나둬야 한다
# 같은 열이 아닌지 (y가 같으면 안됨), 대각선에 있지 않은지 (x-y, x+y가 같으면 안됨)

# 조건은 visited로 만들어준다
visited = [False] * n
visited_2 = [False] * (n * 2 - 1)
visited_3 = [False] * (n * 2 - 1)
answer = 0

def solution(count) : # count가 행
    global answer

    if count == n:
        answer += 1
        return

    for i in range(0,n): # i이 열
        if visited[i] or visited_2[count + i] or visited_3[count - i + n - 1]:
            continue
        visited[i] = True
        visited_2[count + i] = True
        visited_3[count - i + n - 1] = True
        solution(count + 1)
        visited[i] = False
        visited_2[count + i] = False
        visited_3[count - i + n - 1] = False

solution(0)
print(answer)


