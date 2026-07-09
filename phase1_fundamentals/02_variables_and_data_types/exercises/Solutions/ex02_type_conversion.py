def main():
    values = [
        42,
        3.14,
        "123",
        "45.6",
        True,
        False,
        0,
        1,
        "True",
        "False",
        "",
        "0",
    ]

    print("Original Values")
    print("-" * 60)
    for value in values:
        print(f"{repr(value):>8} -> {type(value).__name__}")

    print("\nInteger Conversion")
    print("-" * 60)
    for value in values:
        try:
            print(f"int({repr(value):>8}) = {int(value)}")
        except ValueError as error:
            print(f"int({repr(value):>8}) = ValueError ({error})")

    print("\nFloat Conversion")
    print("-" * 60)
    for value in values:
        try:
            print(f"float({repr(value):>8}) = {float(value)}")
        except ValueError as error:
            print(f"float({repr(value):>8}) = ValueError ({error})")

    print("\nString Conversion")
    print("-" * 60)
    for value in values:
        print(f"str({repr(value):>8}) = {str(value)!r}")

    print("\nBoolean Conversion")
    print("-" * 60)
    for value in values:
        print(f"bool({repr(value):>8}) = {bool(value)}")


if __name__ == "__main__":
    main()