NUMBER = 600851475143

def is_prime(num):
    if num == 2:
        return True
    elif num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def prime_factors(num):
    num1 = num
    factors = []
    while num1 != 1:
        for i in range(2, num):
            if is_prime(i):
                while num1 % i == 0:
                    num1 = num1 // i
                    if i not in factors:
                        factors.append(i)
            if num1 == 1:
                break
    return factors

print(prime_factors(NUMBER))
