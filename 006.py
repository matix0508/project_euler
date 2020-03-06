def sum_of_squares(limit):
    output = 0
    for i in range(1, limit+1):
        output += i ** 2
    return output

def square_of_sum(limit):
    output = 0
    for i in range(1, limit+1):
        output += i
    output = output ** 2
    return output

def main():
    print(square_of_sum(100) - sum_of_squares(100))


if __name__ == "__main__":
    main()
