area = 9
mid = area / 2

try:
    for x in range(area):
        for y in range(area):
            # if y >= x : print(f' *', end=' ')
            if y > x -1 and y < area - x :
                print(f'*', end=' ')
            # if y <= x and y <= area-1 - x: print(f' *', end=' ')
            else: print(f' ', end=' ')
        print()
except Exception as e:
    print(e)