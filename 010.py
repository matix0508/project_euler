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

def primes_below(limit):
    output = []
    for i in range(2, limit):
        if is_prime(i):
            output.append(i)
            print(i)
    return output

def lst_sum(lst):
    output = 0
    for item in lst:
        output += item
    return output

def main():
    print(lst_sum(primes_below(2000000)))

if __name__ == "__main__":
    main()
