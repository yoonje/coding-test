from collections import defaultdict
from operator import itemgetter

sell_num = int(input())
table = defaultdict(int)
for _ in range(sell_num):
    book_name = input()
    table[book_name] += 1

table_list = []
for book_name, value in table.items():
    table_list.append((book_name, value))

print(sorted(sorted(table_list, key=lambda x: x[0]), key=lambda x: x[1], reverse=True))
