def fibonacci():
    """Generate an infinite Fibonacci sequence."""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def main():
    fib = fibonacci()

    print("First 15 Fibonacci numbers:")
    for _ in range(15):
        print(next(fib), end=" ")

    print()


if __name__ == "__main__":
    main()
