from functools import cmp_to_key


def compare(item1, item2, col):
    a, b = item1[1][col], item2[1][col]
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return item1[0] - item2[0]


countSet = input()
for i in range(int(countSet)):
    input()
    items = list(map(lambda x: int(x), input().split(' ')))
    rowCount, colCount = items[0], items[1]
    table = []
    for j in range(rowCount):
        row = list(map(lambda x: int(x), input().split(' ')))
        table += [[j, row]]
    countSort = input()
    sorts = list(map(lambda x: int(x), input().split(' ')))

    for s in sorts:
        table.sort(key=cmp_to_key(lambda x, y: compare(x, y, s-1)))
        for r in range(rowCount):
            table[r][0] = r

    for r in table:
        print(' '.join(str(x) for x in r[1]))
    print()
