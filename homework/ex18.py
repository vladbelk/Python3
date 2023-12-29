try:
    lim = 11
    x = y = 0
    while x < lim:
        while y < lim:
            print(x, y, end=' ')
            if x <= lim - 1 - y and y >=x:

                print(f' *', end=' ')
            else:
                print(f'  ', end=' ')
            y += 1

        x += 1
        y = 0
        print()

except Exception as e:
    print(e)