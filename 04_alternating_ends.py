# Лабораторная работа 5. Задание 4

a = input("Введите элементы массива через пробел: ").split()

result = []
left = 0
right = len(a) - 1

while left < right:
    result.append(a[left])
    result.append(a[right])
    left += 1
    right -= 1

if left == right:
    result.append(a[left])

print(*result)
