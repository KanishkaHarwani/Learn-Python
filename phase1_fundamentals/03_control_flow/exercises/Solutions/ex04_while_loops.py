def collatz_steps(n):
    # TODO: implement using a while loop
    print(n)
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = 3 * n + 1
            print(n)
    pass


if __name__ == "__main__":
    # TODO: test with a few starting numbers, e.g. 1, 6, 27
    number = int(input("Enter a number: "))
    collatz_steps(number)
    pass
