count = input()
for i in range(int(count)):
    countItems = int(input())
    items = input()
    items = list(map(lambda x: int(x), items.split(' ')))
    pair = []
    for i in range(countItems):
        pair.append([i, items[i]])

    while len(pair) >0:
        first = pair[0]
        idx = 1
        diff = abs(pair[idx][1] - pair[0][1])
        other = pair[2:]

        for i in range(len(other)):
            if abs(other[i][1] - first[1]) < diff:
                idx = i+2
                diff = abs(other[i][1] - first[1])

        print(first[0]+1, pair[idx][0]+1)

        pair = pair[:idx]+pair[idx+1:]
        pair = pair[1:]
    print()
