numbers = list(range(1, 16))
# numbers = [1, 3, 0, -4, 1, 2, 6, -10, 0.3]

primes, not_primes = [], []

for number in numbers:
    is_prime = True
    if number <= 1:
        continue
    for divider in range(2, number):
        if number % divider == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

print(f'Numbers: {numbers}')
print(f'Primes: {primes}')
print(f'Primes: {not_primes}')
