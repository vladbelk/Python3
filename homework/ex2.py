try:
    n = int(input( "n = "))
    fact = 1
    for i in range(2, n + 1): fact = fact * i
    print("Факторіл числа", n, " = ", fact)


except Exception as e:
    print(e)