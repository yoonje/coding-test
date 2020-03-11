list = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if list[i] > list[i - 1]:
        descending = False
    elif list[i] < list[i - 1]:
        ascending = False

if ascending is True:
    print("ascending")
elif descending is True:
    print("descending")
else:
    print("mixed")
