def main():
    # Example 1: Dictionary comprehension (word -> length)
    words = [
        "India",
        "Sri Lanka",
        "USA",
        "Canada",
        "Pakistan",
        "United Kingdom",
        "Mexico"
    ]

    word_lengths = {word: len(word) for word in words}

    print("Word Length Dictionary:")
    for word, length in word_lengths.items():
        print(f"{word}: {length}")

    print()

    # Example 2: Set comprehension (numbers divisible by 3)
    numbers = range(1, 31)

    divisible_by_3 = {num for num in numbers if num % 3 == 0}

    print("Numbers divisible by 3:")
    print(divisible_by_3)


if __name__ == "__main__":
    main()
