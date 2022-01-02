
def solution(participant, completion):
    answer = ''
    for  person in participant:
        if person in completion:
            completion.remove(person)
        else:
            answer = person

    return answer
# 효율성 극악

