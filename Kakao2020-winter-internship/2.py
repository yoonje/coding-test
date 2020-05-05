import copy


def solution(s):
    s = s[2:len(s) - 2].split("},{")
    set_list = list()
    for item in s:
        set_list.append(list(map(int, (item.split(",")))))
    set_list.sort(key=lambda x: len(x))
    for idx in range(1, len(set_list)):
        if set(set_list[idx]).issuperset(set(set_list[idx - 1])) is True:
            item = copy.deepcopy(set_list[idx])
            for temp in set_list[idx - 1]:
                item.remove(temp)
            val = copy.deepcopy(set_list[idx - 1])
            val.extend(item)
            set_list[idx] = val
    return set_list[-1]
