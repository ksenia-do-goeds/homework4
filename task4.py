def decorator_info(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator_info
def calculate_area(length, width):
    return length width

# Пример использования:
area = calculate_area(5, 10)
print(f"Площадь прямоугольника: {area}")

area2 = calculate_area(length=7, width=3)
print(f"Площадь прямоугольника: {area2}")


