# Лабораторная работа 5. Задание 8

from decimal import Decimal

a = list(map(Decimal, input("Введите элементы массива через пробел: ").split()))
even_positions = a[1::2]

if even_positions:
    print(min(even_positions))
else:
    print("В массиве нет элементов с четными номерами.")
