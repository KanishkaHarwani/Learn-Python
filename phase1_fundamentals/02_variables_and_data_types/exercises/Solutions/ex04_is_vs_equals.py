def main():
    # Small integers (cached by Python)
    val_0 = 1
    val_1 = 1

    val_2 = 10
    val_3 = 10

    val_4 = 100
    val_5 = 100

    # Large integers (created at runtime)
    val_6 = int("1000")
    val_7 = int("1000")

    # Strings (one created at runtime)
    val_8 = "1000"
    val_9 = "".join(["10", "00"])

    print(f"'==' check for {val_0}: {val_0 == val_1}")
    print(f"'is' check for {val_0}: {val_0 is val_1}\n")

    print(f"'==' check for {val_2}: {val_2 == val_3}")
    print(f"'is' check for {val_2}: {val_2 is val_3}\n")

    print(f"'==' check for {val_4}: {val_4 == val_5}")
    print(f"'is' check for {val_4}: {val_4 is val_5}\n")

    print(f"'==' check for {val_6}: {val_6 == val_7}")
    print(f"'is' check for {val_6}: {val_6 is val_7}\n")

    print(f"'==' check for {val_8}: {val_8 == val_9}")
    print(f"'is' check for {val_8}: {val_8 is val_9}")


if __name__ == "__main__":
    main()