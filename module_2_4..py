#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        else:
            not_primes.append(num)
    else:
        not_primes.append(num)
print('primes', primes)
print('not_primes', not_primes)