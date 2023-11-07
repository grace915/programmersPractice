import sys
input = sys.stdin.readline

W, N = map(int, input().split())

array = []

for _ in range(N):
    array.append(list(map(int, input().split())))
print(array)