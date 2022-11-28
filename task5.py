# Реализуйте алгоритм перемешивания списка.

import random

list = [1, 2, 3, 4, 5, 6, 7, 8]
# random.shuffle(list)
# print(list)

from random import randint
for i in range(len(list)-1):
    tmp = list[i]
    rmdNumber = random.randint(0, len(list) - 1)
    list[i] = list[rmdNumber]
    list[rmdNumber] = tmp
print(list)
