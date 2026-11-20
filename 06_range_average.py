# Лабораторная работа 5. Задание 6

a = list(map(float, input("Введите элементы массива через пробел: ").split()))
k, l = map(int, input("Введите K и L через пробел: ").split())

selected = a[k - 1:l]
average = sum(selected) / len(selected)

print(average)
