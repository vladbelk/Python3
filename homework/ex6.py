try:
   start = int(input("Введіть початок діапазону: "))
   end = int(input("Введіть кінець діапазону: "))


   print("Всі числа діапазону:")
   for i in range(start, end + 1):
       print(i)

   print("Всі числа діапазону в спадному порядку:")
   for i in range(end, start - 1, -1):
       print(i)

   print("Всі числа, кратні 7:")
   for i in range(start, end + 1):
       if i % 7 == 0:
           print(i)

   count = 0
   for i in range(start, end + 1):
       if i % 5 == 0:
           count += 1
   print("Кількість чисел, кратних 5:", count)

except Exception as e:
    print(e)