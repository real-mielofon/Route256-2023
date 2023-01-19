countSet = input()
for i in range(int(countSet)):
    count = input()
    items = list(map(lambda x: int(x), input().split(' ')))
    last, dict = items[0], {items[0]:1}
    for t in items[1:]:
        if t == last:
            continue
        if t in dict:
            print('NO')
            break
        last, dict[t] = t, 1
    else:
        print('YES')
