# Лабораторная работа 5. Задание 5

a = input("Введите элементы массива через пробел: ").split()

odd_positions = a[::2]
even_positions = a[1::2]

print(*odd_positions, *reversed(even_positions))
