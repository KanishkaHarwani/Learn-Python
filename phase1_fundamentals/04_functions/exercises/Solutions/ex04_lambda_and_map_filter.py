def main():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print(f"This is the list of values: {values}")
    print()

    # Multiplies each value by 2
    print("Multiplying all values by 2 using lambda and map()")
    print(list(map(lambda x: x * 2, values)))
    print()

    # only prints even values
    print("Eliminating all odd values using lambda and filter()")
    print(list(filter(lambda x: x % 2 == 0, values)))

    pass


if __name__ == "__main__":
    main()
