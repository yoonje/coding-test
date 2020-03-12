num, search_seq = list(map(int, input().split(' ')))
data_list = list(map(int, input().split(' ')))
data_list.sort()
print(data_list[search_seq - 1])
