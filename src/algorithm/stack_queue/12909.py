
def solution(s):
    answer = True
    stack = []
    for word in s:
        if word == '(':
            stack.append(word)
        if word == ')':
            if len(stack) == 0:
                answer = False
                break
            stack.pop()

    if len(stack) != 0:
        answer = False
    return answer