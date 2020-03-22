person_num = int(input())
reward_list = list()


def game(num_list):
    num_set = set(num_list)
    if len(num_set) == 1:
        return 50000 + num_list[0] * 5000
    elif len(num_set) == 2:
        if num_list[1] == num_list[2]:
            return 10000 + num_list[1] * 1000
        else:
            return 2000 + (num_list[1] + num_list[2]) * 500
    elif len(num_set) == 3:
        temp_list = list(num_set)
        for item in temp_list:
            num_list.remove(item)
        return 1000 + num_list[0] * 100
    else:
        return num_list[-1] * 100


for i in range(person_num):
    num_list = list(map(int, input().split()))
    reward_list.append(game(sorted(num_list)))
print(max(reward_list))
