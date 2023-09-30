import itertools
import re
def solution(numbers):

    answer = ''
    numbers = [str(number) for number in numbers]
    numbers.sort(key = lambda x:x*3, reverse=True)

    for number in numbers:
        answer += number

    return str(int(''.join(numbers)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0,0]))