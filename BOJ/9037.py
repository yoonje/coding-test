import copy

test_case = int(input())

circuit_count_list = 0


def f(candy_list, child_num):
    temp_candy_list = copy.deepcopy(candy_list)
    for i in range(child_num):
        temp_candy_list[i] = temp_candy_list[i] // 2
        temp_candy_list[i] += candy_list[i - 1] // 2
    candy_list = temp_candy_list
    for i in range(child_num):
        if candy_list[i] % 2 != 0:
            candy_list[i] += 1
    return candy_list


for _ in range(test_case):
    child_num = int(input())
    candy_list = list()
    candy_list.extend(list(map(int, (input().split()))))
    for i in range(child_num):
        if candy_list[i] % 2 != 0:
            candy_list[i] += 1
    count = 0
    while min(candy_list) != max(candy_list):
        candy_list = f(candy_list, child_num)
        count += 1
    print(count)
