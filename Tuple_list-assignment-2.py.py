tuple= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
for i in tuple:
    tuple.sort(key = lambda x: x[-1])
    print(tuple)
    