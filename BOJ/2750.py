test_case = int(input())
num_list = list()
for _ in range(test_case):
    num_list.append(int(input()))
num_list.sort()
for item in num_list:
    print(item)
