# Лабораторная работа 5. Задание 7

a = list(map(int, input("Введите элементы массива через пробел: ").split()))

difference = 0
if len(a) >= 2:
    difference = a[1] - a[0]
    for i in range(2, len(a)):
        if a[i] - a[i - 1] != difference:
            difference = 0
            break

print(difference)
