# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 17 -> Вывод: 1, 2, 4, 8, 16

number = int(input("Введите натуральное число: "))
result = []
step = 1

if number < 1:
    print(f"Введено некорректное значение.")
else:
    while step <= number:
        result.append(step)
        step = 2 * step
    print(f"Ввод: {number} -> Вывод: {result}")
