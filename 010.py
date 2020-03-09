
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

def progres_bar(current, max):
    print(f"Progress: {100 * current / max} %")

def primes_below(limit):
    output = [2]
    for i in range(3, limit):
        add = True
        for item in output:
            if i % item == 0:
                add = False
        if add:
            output.append(i)
            progres_bar(i, limit)
    return output

def lst_sum(lst):
    output = 0
    for item in lst:
        output += item
    return output

def main():
    pass
    print(lst_sum(primes_below(2000000)))

if __name__ == "__main__":
    main()
