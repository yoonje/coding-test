table_list_num = int(input())
table_set = set(map(int, input().split(' ')))
search_list_num = int(input())
search_list = list(map(int, input().split(' ')))
for item in search_list:
    if item in table_set:
        print("1")
    else:
        print("0")
