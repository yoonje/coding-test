import sys

milk_list = list()

for _ in range(3):
    a, b = map(int, input().split())
    milk_list.append([a, b])

count = 0
while True:
    for i in [1, 2, 0]:
        if milk_list[i][1] + milk_list[i - 1][1] > milk_list[i][0]:
            milk_list[i - 1][1] -= milk_list[i][0] - milk_list[i][1]
            milk_list[i][1] = milk_list[i][0]
        else:
            milk_list[i][1] += milk_list[i - 1][1]
            milk_list[i - 1][1] = 0
        count += 1
        if count == 100:
            for item in milk_list:
                print(item[1])
            sys.exit()
