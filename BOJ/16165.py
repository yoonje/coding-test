girl_group_num, problem_num = list(map(int, input().split()))

girl_group_table = dict()

for _ in range(girl_group_num):
    group_name = input()
    member_num = int(input())
    member_list = list()
    for _ in range(member_num):
        member_list.append(input())
    girl_group_table[group_name] = member_list

problem_list = list()

for _ in range(problem_num):
    problem_info = input()
    problem_type = int(input())
    problem_list.append([problem_type, problem_info])

for i in range(problem_num):
    if problem_list[i][0] == 1:
        for value in girl_group_table.items():
            if problem_list[i][1] in value[1]:
                print(value[0])
    else:
        for value in girl_group_table.items():
            if problem_list[i][1] in value[0]:
                temp_member_list = sorted(value[1])
                for member in temp_member_list:
                    print(member)
