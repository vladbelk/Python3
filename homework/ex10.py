try:
    x = 5
    y = 5

    i = j = 0
    while i < x:
        while j < y:
            if i <= j:
                print(f' * ', end=' ')
            else:
                print(f' ', end=' ')
            j+=1
        i+= 1
        j= 0
        print()

except Exception as e:
    print(e)