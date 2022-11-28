#  Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.
#  (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

n = int(input('Введите число  '))
list = []

if n < 0:
    n *= -1
for i in range(n*2+1):
    list.append(-n + i)
print(list)

file = open('HomeWorkPython 25.11.22/file.txt', 'r')
pos1 = int(file.readline())
pos2 = int(file.readline())
file.close

print( pos1, ',', pos2)


if pos1 >= len(list) or pos1 < 0 or pos2 >= len(list) or pos2 < 0:
    print('Неверные позиции !!!')

else:
    print(f'Сумма  ', int(list[pos1]) + int(list[pos2]))
