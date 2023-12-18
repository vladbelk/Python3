try:
    a = int(input("Перше число = "))
    b = int(input("Друге число = "))
    s = 0
    for i in range(a, b+1):
        s = s + a

    print(f"Сума чисел в діапазоні = {s}")
    print(f"Середнє арифметичне двух = {(a + b) / 2} ")
    print(f"Середнє арифметичне всіх = {s / (b - a)} ")


except Exception as e:
    print(e)