# Лабораторная работа 5. Задание 9

from decimal import Decimal

a = list(map(Decimal, input("Введите элементы массива через пробел: ").split()))

position = 0
for i in range(len(a) - 1, -1, -1):
    greater_than_left = i == 0 or a[i] > a[i - 1]
    greater_than_right = i == len(a) - 1 or a[i] > a[i + 1]
    if greater_than_left and greater_than_right:
        position = i + 1
        break

print(position)
