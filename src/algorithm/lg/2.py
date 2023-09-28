import re


def solution(deposit):
    # deposit: ["입금자명 입금액"]
    sum = 0
    deposits = ' '.join(s for s in deposit)
    print(deposits)
    #
    result = re.finditer(
        r'.?alary ([0-9]+)|s.?lary ([0-9]+)|sa.?ary ([0-9]+)| sal.?ry ([0-9]+)| sala.?y ([0-9]+)| salar.? ([0-9]+)',
        deposits)
    # print(result)
    for i in result:
        print(i.groups())
        sum += int(i.groups()[0])
    # result1 = re.findall(r'.?alary ([0-9]+)', deposits)
    # result2 = re.findall(r's.?lary ([0-9]+)', deposits)
    # result3 = re.findall(r'sa.?ary ([0-9]+)', deposits)
    # result4 = re.findall(r'sal.?ry ([0-9]+)', deposits)
    # result5 = re.findall(r'sala.?y ([0-9]+)', deposits)
    # result6 = re.findall(r'salar.? ([0-9]+)', deposits)
    # result = result1 + result2 + result3 + result4 + result5 + result6
    print(sum)

    # sum += int(result[0][0]) + int(result[1][0]) + int(result[2][0])
    # print(sum)
    # print(int(result[0][0]))



solution(["salary 10000", "alary 20000", "saary 30000", "sallry 40000", "salay 50000", "salarr 60000"])
