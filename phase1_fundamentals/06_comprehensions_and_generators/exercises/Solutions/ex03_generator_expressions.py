import sys

def main():
    # List comprehension
    squares_comp = [i ** 2 for i in range(20)]

    # Equivalent generator expression
    squares_gen = (i ** 2 for i in range(20))

    # Compare memory usage
    print("Memory Comparison")
    print("-----------------")
    print(f"List size      : {sys.getsizeof(squares_comp)} bytes")
    print(f"Generator size : {sys.getsizeof(squares_gen)} bytes")

    print("\nList contents:")
    print(squares_comp)

    print("\nGenerator object:")
    print(squares_gen)

    print("\nGenerator contents:")
    for value in squares_gen:
        print(value, end=" ")
    print()


if __name__ == "__main__":
    main()
