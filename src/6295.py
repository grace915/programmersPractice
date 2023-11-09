import sys
input = sys.stdin.readline

T = int(input())
test_cases = []

for _ in range(T):
    test_cases.append(list(map(int, input().split())))

def solution(a, b):
    return a + b


answer = []

for i in range(len(test_cases)):
    a, b = test_cases[i]
    print("Case #%d: %d" %(i+1, solution(a, b)))