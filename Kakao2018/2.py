import re

db = {'S': '**1', 'D': '**2', 'T': '**3', '#': '*-1', }


def solution(dartResult):
    answer = ""
    ret_list = re.findall(r'\d+[SDT*#]+', dartResult)
    for idx, item in enumerate(ret_list):
        if item[-1] == "*":
            if answer:
                answer = answer[:-1] + '*2+'
            item += '2'
        for j in db.keys():
            item = item.replace(j, db[j])
        answer += item + '+'
    return eval(answer[:-1])


print(solution('1S2D*3T'))
