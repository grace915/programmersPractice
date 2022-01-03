import collections

def solution(phone_book):
    answer = True
    #phonebook = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1, 0):
            return False

    return answer

# find(문자, 위치)
# startswith(시작문자, 시작지점)
# endswith(끝나는문자, 문자열시작, 문자열끝)

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))