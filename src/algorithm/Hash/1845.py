def solution(nums):
    # 4마리 -> 3123 / 3 2마리, 1 1마리, 2번 1마리
    # 31, 32, 33, 12, 13, 23
    # n/2마리의 폰켓몬 선택.

    # 333224
    # 324

    num = len(nums) / 2
    dic = {}
    nums.sort()

    check = 0
    temp = 0
    for n in nums:
        if temp != n:
            temp = n
            check = check + 1

    answer = 0
    if check > num:
        answer = num
    else:
        answer = check
    return answer


# 다른 사람 풀이
def solution(nums):
    answer = 0
    myList = set(nums)
    if len(nums) / 2 > len(myList):
        answer = len(myList)
    else:
        answer = len(nums) / 2
    return answer