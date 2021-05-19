# первый пример
# n = 5
# while n>0:
#     print(n)
#     n = n - 1
# else:
#     print("СТОП")
# print(n)

# второй пример

# n = 5
# while n>0:
#     print("HI", n)
#     n = n - 3
# print("STOP")

#ТРЕТИЙ ПРИМЕР бесконечный цикл
# a = 1
# while a > 0:
#     print(a)
#     a = a + 1

# ЧЕТВЕРТЫЙ ПРИМЕР бесконечный цикл
# while True:
#     print("HI")
#     print("Students")
# print("STOP")

# ПЯТЫЙ ПРИМЕР выход с цикла
# while True:
#     line = input('> ')
#     if line == 'остановись':
#         break
#     print(line)
# print("ВСЕ")

# ПРИМЕР CONTINUE
# n = 10
# while n > 0:
#     n = n - 1
#     if n == 5:
#         continue
#
#     print("Hi", n)
# print("Все")

# ПРИМЕР PASS
# n = 10
# while n > 0:
#     n = n - 1
#     if n == 5:
#         pass
#     print("Number is: ", n)
# print("STOP")
# С оператором pass программа работает так, будто в ней нет условных
# операторов. Оператор pass говорит программе игнорировать это условие и продолжать работу.


#По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания.
# a = int(input())
# i = 1
# while i**2 <= a:
#     print(i**2)
#     i += 1

#task 2
#Дано целое число, не меньшее 2. Выведите его наименьший простой делитель.
# n = int(input())
# i = 2
# while n%i!=0:
#     i+=1
# print(i)

#task 3
#По данному числу N распечатайте все целые степени двойки, не превосходящие N, в порядке возрастания.
# n = int(input())
# i = 1
# while i < n:
#     print(i, end=' ')
#     i=i*2

#task 4
#Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки, или слово NO в противном случае.
# n = int(input())
# i = 2
# while i != n:
#     if i > n:
#         print("NO")
#         break
#     i = i * 2
# else:
#     print("OOK")

#task 5
#По данному натуральному числу N выведите такое наименьшее целое число k, что 2k≥N.
# n = int(input())
# i = 0
# while i ** 2 < n:
#     i = i + 1
# print(i)











