LIMIT = 4000000

def get_fibonnaci():
    fibonnaci = [1, 2]
    while fibonnaci[-1] < LIMIT:
        fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
    return fibonnaci

def sum_if_even(lst):
    output = 0
    for item in lst:
        if item % 2 == 0:
            output += item
    return output

def main():
    print(sum_if_even(get_fibonnaci()))

if __name__ == "__main__":
    main()
