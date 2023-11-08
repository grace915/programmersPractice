import sys
input = sys.stdin.readline

N = int(input())
rocks = list(map(int, input().split()))

now = 0
answer = 0
for rock in rocks:
  if now < rock:
    now = rock
    answer += 1
print(answer)
