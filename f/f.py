from datetime import datetime
from functools import cmp_to_key

countSet = int(input())


def compare(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0


def checkCrossTime(times, k):
    times.sort(key=cmp_to_key(lambda x, y: compare(x, y)))
    global j
    for i in range(1, len(times)):
        first = times[i - 1]
        second = times[i]
        if first[1] < second[0] or second[1] < first[0]:
            continue
        print("NO")
        return
    else:
        print("YES")


for k in range(countSet):
    count = int(input())
    times = []
    exitFlag = False
    for j in range(count):
        pair = input().strip().split('-')
        if exitFlag:
            continue
        try:
            left = datetime.strptime(pair[0], '%H:%M:%S')
            right = datetime.strptime(pair[1], '%H:%M:%S')
        except:
            print("NO")
            exitFlag = True
            continue

        if left > right:
            print("NO")
            exitFlag = True
            continue
        times += [[left, right]]

    if not exitFlag:
        if len(times) > 1:
            checkCrossTime(times, k)
        else:
            print("YES")
