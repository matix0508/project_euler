def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def all_prime(lst):
    for item in lst:
        if not is_prime(item):
            return False
    return True

def factorise(num):
    output = []
    num1 = num
    while not is_prime(num1):
        for i in range(2, num1):
            if num1 % i == 0:
                num1 = num1 // i
                output.append(i)
                if is_prime(num1):
                    output.append(num1)
                break
    return output


def get_divisors(num):
    output = []
    for i in range(2, num+1):
        if num % i == 0:
            if is_prime(i):
                output.append(i)
            else:
                pass
    return output


def all_divisors(limit):
    output = []
    for i in range(2, limit + 1):
        lst = get_divisors(i)
        for item in lst:
            if item not in output:
                output.append(item)

    print(f"lst: {output}")
    return output

def product_lst(lst):
    output = 1
    for item in lst:
        output *= item
    return output

def main():
    print(product_lst(all_divisors(20)))


print(factorise(68))
#if __name__ == "__main__":
#    main()
