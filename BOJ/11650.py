n = int(input())
location_list = []
for _ in range(n):
    input_data = input().split(' ')
    location_list.append((int(input_data[0]), int(input_data[1])))
location_list = sorted(location_list)
for item in location_list:
    print(item[0], item[1])
