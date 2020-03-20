N, M = list(map(int, input().split()))
name, name2 = input().split()

table = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 2,
    "E": 4,
    "F": 3,
    "G": 1,
    "H": 3,
    "I": 1,
    "J": 1,
    "K": 3,
    "L": 1,
    "M": 3,
    "N": 2,
    "O": 1,
    "P": 2,
    "Q": 2,
    "R": 2,
    "S": 1,
    "T": 2,
    "U": 1,
    "V": 1,
    "W": 1,
    "X": 2,
    "Y": 2,
    "Z": 1,
}


def check_compatibility(score_list):
    temp_list = list()
    for i in range(1, len(score_list)):
        temp_list.append((score_list[i - 1] + score_list[i]) % 10)
    return temp_list


mixed_name = ""

max_len = max([M, N])

for i in range(max_len):
    try:
        mixed_name += name[i] + name2[i]
    except IndexError:
        break

if len(name) > len(name2):
    mixed_name += name[i:]
elif len(name) < len(name2):
    mixed_name += name2[i:]

score_list = list()

for i in range(len(mixed_name)):
    score_list.append(table[mixed_name[i]])

while len(score_list) != 2:
    score_list = check_compatibility(score_list)

print("{}%".format(str(score_list[0] * 10 + score_list[1])))
