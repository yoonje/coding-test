def update_uid_table(item, uid_table):
    if item[0] == "Enter" and (uid_table.get(item[1]) is None):
        uid_table[item[1]] = item[2]
    elif item[0] == "Change" and (uid_table.get(item[1]) is None):
        uid_table[item[1]] = item[2]
    return uid_table


def solution(record):
    uid_table = {}
    answer = []
    for i in range(len(record) - 1, -1, -1):
        uid_table = update_uid_table(record[i].split(), uid_table)
    for j in range(0, len(record)):
        record_list = record[j].split()
        if record_list[0] == "Enter":
            answer.append(uid_table[record_list[1]] + "님이 들어왔습니다.")
        elif record_list[0] == "Leave":
            answer.append(uid_table[record_list[1]] + "님이 나갔습니다.")
    return answer
