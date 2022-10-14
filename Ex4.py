# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
n = int(input('Введите размер списка: '))
m = int(input('Введите первую позицию: '))
k = int(input('Введите вторую позицию: '))

numbers = []
for i in range(n):
    numbers.append(random.randint(-n, n + 1))
print(f'Список:\n {(numbers)}')

with open('file.txt', 'w') as data:
    data.write(f'{m}\n')
    data.write(f'{k}\n')

def file_data(list: numbers) -> int:
   path = 'file.txt'
   file_num = open(path, 'r')
   sum = 1
   for line in file_num:
    sum = sum * list[int(line)]
   file_num.close()
   return sum
print(f'Произведение позиций: {file_data(numbers)}')