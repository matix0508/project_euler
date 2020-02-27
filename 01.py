LIMIT = 1000
#new comment

def multiple(num):
    if num % 5 == 0 or num % 3 == 0:
        return True
    else:
        return False

def main():
    output = 0
    for i in range(LIMIT):
        if multiple(i):
            output += i
    print(output)

if __name__ == "__main__":
    main()
