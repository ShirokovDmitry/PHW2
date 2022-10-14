# Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму.

n = int(input('Введите число: '))
list = [round((1 + 1/n)**n, 2) 
    for n in range(1, n + 1)]
print(list)
print(sum(list))
