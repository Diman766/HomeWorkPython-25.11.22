# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = input('Введите число  ')
result = 0

for i in range(len(number)):
    result += int(number[i])
print(result)
