def timeToMinute(time):
    lst = time.split(':')
    return int(lst[0]) * 60 + int(lst[1])


def minuteToTime(minute):
    div, mod = divmod(minute, 60)
    return "%02d:%02d" % (div, mod)


def crewTime(timetable):
    return [timeToMinute(time) for time in timetable]


def shuttleTime(n, t, start='09:00'):
    shuttle = [timeToMinute(start)]
    for n1 in range(n - 1):
        shuttle.append(shuttle[-1] + t)
    return shuttle


def duplicateTime(c, integrate):
    if not c in integrate.keys():
        return c
    else:
        return duplicateTime(c + 0.001, integrate)


def solution(n, t, m, timetable):
    crew = sorted(crewTime(timetable))
    shuttle = shuttleTime(n, t)
    conTime = set(shuttle + crew)
    for c in set(crew):
        conTime.add(c - 1)
    for con in sorted(list(conTime))[::-1]:
        integrate = dict()
        for c in crew:
            integrate[duplicateTime(c, integrate)] = 'crew'
        integrate[duplicateTime(con, integrate)] = 'con'
        for sh in shuttle:
            integrate[duplicateTime(sh, integrate)] = 'shuttle'
        waiting_line = []
        for time in sorted(integrate.keys()):
            if 'crew' == integrate[time]:
                waiting_line.append('crew')
            elif 'con' == integrate[time]:
                waiting_line.append('con')
            elif 'shuttle' == integrate[time]:
                waiting_line = waiting_line[m:]
        if 'con' not in waiting_line:
            return minuteToTime(con)
