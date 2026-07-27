def main():
    # Example 1: Build a list of numbers
    numbers_loop = []
    for i in range(10):
        numbers_loop.append(i)

    numbers_comp = [i for i in range(10)]

    # Example 2: Build a list of squares
    squares_loop = []
    for i in range(10):
        squares_loop.append(i ** 2)

    squares_comp = [i ** 2 for i in range(10)]

    # Example 3: Build a list of even numbers
    evens_loop = []
    for i in range(20):
        if i % 2 == 0:
            evens_loop.append(i)

    evens_comp = [i for i in range(20) if i % 2 == 0]

    # Print results
    print(f"Numbers (Loop):         {numbers_loop}")
    print(f"Numbers (Comprehension): {numbers_comp}\n")

    print(f"Squares (Loop):         {squares_loop}")
    print(f"Squares (Comprehension): {squares_comp}\n")

    print(f"Evens (Loop):         {evens_loop}")
    print(f"Evens (Comprehension): {evens_comp}")


if __name__ == "__main__":
    main()
