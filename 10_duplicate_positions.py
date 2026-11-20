# Лабораторная работа 5. Задание 10

a = list(map(int, input("Введите элементы массива через пробел: ").split()))

first_positions = {}
for position, value in enumerate(a, start=1):
    if value in first_positions:
        print(first_positions[value], position)
        break
    first_positions[value] = position
