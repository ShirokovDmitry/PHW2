# Реализуйте алгоритм перемешивания списка.
# random.shuffle(list) - простой способ
import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Список: \n', list)
new = len(list)

for i in range(new):
    k = random.randint(0, new - 1)
    new_num = list.pop(k)
    list.append(new_num)
print('Новый список: \n',list)


