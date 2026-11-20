# Лабораторная работа 5. Задание 3

n, first, second = map(int, input("Введите N, A и B через пробел: ").split())

a = [first, second]
total = first + second
for _ in range(2, n):
    a.append(total)
    total += a[-1]

print(*a)
