import math

def solution(plants, demand, power):
    # output은 신규 발전소의 개수
    # plants는 준공연도, 설계수명, 발전량
    # demand는 2050 전력 수요량
    # power은 신규 발전소의 발전량

    sum = 0
    for plant in plants:
        if plant[0] + plant[1] >= 250:
            sum += plant[2]
    return math.ceil((demand - sum) / power)

