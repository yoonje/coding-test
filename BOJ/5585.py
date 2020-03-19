price = int(input())

money = 1000 - price

count = 0
for i in [500, 100, 50, 10, 5, 1]:
    count += money // i
    money %= i
print(count)
