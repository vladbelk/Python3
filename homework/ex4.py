try:
   length = int(input("Введіть довжину лінії: "))
   symbol = input("Введіть символ: ")

   print(length * symbol)

except Exception as e:
    print(e)