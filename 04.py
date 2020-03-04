def is_palindromic(num):
    num_str = str(num)
    len_num = len(num_str)
    if len_num % 2 == 0:
        counter = len_num // 2
    else:
        counter = (len_num - 1) // 2
    for i in range(counter):
        if num_str[i] != num_str[-i-1]:
            return False
    return True

def product_lst():
    output = []
    for i in range(1, 100):
        for j in range(1, 100):
            a = 1000 - i
            b = 1000 - j
            if is_palindromic(a * b):
                output.append(a * b)
    return output

def get_max(lst):
    output = lst[0]
    for item in lst:
        if item > output:
            output = item
    return output

def main():
    print(get_max(product_lst()))


if __name__ == "__main__":
    main()
