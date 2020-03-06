def nth_prime(limit):
    output = [2]
    add = True
    i = 2
    while len(output) < limit:
        add = True
        for item in output:
            if i % item == 0:
                add = False
                break
        if add:
            output.append(i)
        i += 1
    return output[-1]

def main():
    print(nth_prime(10001))

if __name__ == "__main__":
    main()
