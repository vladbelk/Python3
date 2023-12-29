try:
    x = 4
    y = 7

    i = j = 0
    wall = x - 1
    counter = 0
    while i < y:
        j = 0
        if i > int(y / 2):
            counter += 1
        while j < x:
            # print(f'[{i},{j}]', end=' ')
            if i <= int(y / 2):
                if i >= j:
                    print(f' *', end=' ')
                else:
                    print(f'     ', end=' ')
            else:
                if j <= wall - counter:
                    print(f' *' , end=' ')
                else:
                    print(f'     ', end=' ')
            j += 1
        print()
        i += 1
except Exception as e:
    print(e)