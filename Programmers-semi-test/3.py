def solution(v):
    x_list = [item[0] for item in v]
    y_list = [item[1] for item in v]
    answer = list()
    for i in x_list:
        if x_list.count(i) == 1:
            answer.append(i)
    for j in y_list:
        if y_list.count(j) == 1:
            answer.append(j)
    return answer
