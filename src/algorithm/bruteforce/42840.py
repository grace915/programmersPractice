def solution(answers):

    one, two, three = 0, 0, 0
    one_answer = [1,2,3,4,5]
    two_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    three_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        now = answers[i]
        #print(now)
        # 1번
        if now == one_answer[i % 5]:
            one += 1
        # 2번
        if now == two_answer[i % 8]:
            two += 1
         # 3번
        if now == three_answer[i % 10]:
            three += 1

    answer = []
    value = max(one, two, three)
    if value == one:
        answer.append(1)
    if value == two:
        answer.append(2)
    if value == three:
        answer.append(3)


    return answer



print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))