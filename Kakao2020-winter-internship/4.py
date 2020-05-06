import sys

sys.setrecursionlimit(1000)


def find_empty_room(x, room_dict):
    if x not in room_dict:
        room_dict[x] = x + 1
        return x
    p = find_empty_room(room_dict[x], room_dict)
    room_dict[x] = p + 1
    return p


def solution(k, room_number):
    room_dict = dict()
    answer = list()
    for room in room_number:
        empty_room = find_empty_room(room, room_dict)
        answer.append(empty_room)
    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))  # [1,3,4,2,5,6]
