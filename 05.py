def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
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

def how_many(lst, num):
    output = 0
    for item in lst:
        if item == num:
            output += 1
    return output

def all_factors(limit):
    output = []
    for i in range(2, limit + 1):
        factors = factorise(i)
        for item in factors:
            while how_many(factors, item) > how_many(output, item):
                output.append(item)
    return output




def product_lst(lst):
    output = 1
    for item in lst:
        output *= item
    return output

def main():
    print(product_lst(all_factors(20)))


#print(factorise(68))
if __name__ == "__main__":
    main()
