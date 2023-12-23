try:
   length = int(input("Введіть довжину лінії: "))

   print("*" * length)

except Exception as e:
    print(e)