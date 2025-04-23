'''
1. Создайте список квадратов первых 10 натуральных чисел, используя list comprehension.
'''
n = [i**2 for i in range(1, 11)]
print(n)
'''
2. Создайте словарь, содержащий названия дней недели и их порядковые номера, используя dict comprehension.
Для дней недели можно использовать список ["Понедельник", "Вторник" и т.д.]
'''
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day_numbers = {day: i + 1 for i, day in enumerate(days)}
print(day_numbers)
'''
3. Создайте множество, содержащее теги библиотек в нижнем регистре, используя list comprehension.
Исходный список ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
'''
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_set = {lib.lower() for lib in tags}
print(tags_set)
'''
4. Создайте список, содержащий только четные числа из исходного списка, используя list comprehension.
Исходный список [1, 3, 4, 87, 98, 15, 7, 4]
'''
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)
'''
5. Создайте словарь, где ключи — это числа от 1 до 5, а значения — их факториалы, используя dict comprehension.
Для вычисления факториала импортируйте функцию factorial из модуля math, либо реализуйте вычисление факториала самостоятельно.
'''
from math import factorial
factorials_dict = {i: factorial(i) for i in range(1, 6)}
print(factorials_dict)
