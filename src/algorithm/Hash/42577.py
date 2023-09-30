def solution(phone_book):
    answer = True
    hash = {}

    for phone in phone_book:
        hash[phone] = 1

    for phone in phone_book:
        now = ''
        for i in phone:
            now += i
            if now in hash and now != phone:
                answer = False
                break
    return answer


solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])