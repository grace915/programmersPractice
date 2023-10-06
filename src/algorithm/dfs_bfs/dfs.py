

visited = [False] * 11
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def dfs(x): # x가 index라고 생각
    visited[x] = True
    print(x)

    for i in range(len(array[x])):
        if not visited[array[x][i]]:
            dfs(array[x][i])


dfs(0)

