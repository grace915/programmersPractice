import sys
input = sys.stdin.readline

N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort(key=lambda x:x[1])
# print(classes)
answer = [classes[0]]
for i in range(1, len(classes)):
  start, end = classes[i]
  if start >= answer[-1][1]:
    answer.append([start, end])

print(len(answer))