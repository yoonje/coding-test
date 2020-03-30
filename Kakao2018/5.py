import re
import copy


def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    str1_list = list()
    str2_list = list()
    while str1:
        if re.match(r'[a-zA-Z]{2}', str1) is not None:
            str1_list.append(re.match(r'[a-zA-Z]{2}', str1).group())
        str1 = str1[1:]
    while str2:
        if re.match(r'[a-zA-Z]{2}', str2) is not None:
            str2_list.append(re.match(r'[a-zA-Z]{2}', str2).group())
        str2 = str2[1:]
    intersection = list()
    temp_str_list = copy.deepcopy(str2_list)
    for item in str1_list:
        if item in temp_str_list:
            intersection.append(item)
            temp_str_list.remove(item)
    union = str1_list + str2_list
    for item in intersection:
        union.remove(item)
    if len(union) == 0:
        return 65536
    return int(len(intersection) / len(union) * 65536)


print(solution('E=M*C^2', 'e=m*c^2'))
