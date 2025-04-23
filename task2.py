import math

def prime_generator():
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1

# Пример использования:
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))

