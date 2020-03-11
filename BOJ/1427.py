num = input()
digit_list = list()
for idx in range(len(num)):
    digit_list.append(num[idx])
digit_list.sort(reverse=True)
print("".join(digit_list))
