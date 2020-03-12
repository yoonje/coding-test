bird_num = int(input())
remain_bird_num = bird_num
count = 0
i = 0
while True:
    remain_bird_num -= i
    if remain_bird_num > 0:
        count += 1
        i += 1
    elif remain_bird_num < 0:
        remain_bird_num += i
        i = 1
    else:
        print(count)
        break
