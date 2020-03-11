n = int(input())
member_list = []
for _ in range(n):
    input_data = input().split(' ')
    member_list.append((int(input_data[0]), input_data[1]))
member_list = sorted(member_list, key=lambda x: x[0])
for i in member_list:
    print(i[0], i[1])