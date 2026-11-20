# Лабораторная работа 5. Задание 2

from decimal import Decimal

n = int(input("Введите N: "))
first, ratio = map(Decimal, input("Введите A и D через пробел: ").split())

a = [first]
for _ in range(1, n):
    a.append(a[-1] * ratio)

print(*(format(value, "f") for value in a))
