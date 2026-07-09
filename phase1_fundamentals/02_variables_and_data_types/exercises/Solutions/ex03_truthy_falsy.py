def main():
    def check_truthy(value):
        if value:
            return "Truthy"
        else:
            return "Falsy"

    print(f"Truthy/Falsy for 10 is {check_truthy(10)}")
    print(f"Truthy/Falsy for 0 is {check_truthy(0)}")
    print(f"Truthy/Falsy for 'Hello' is {check_truthy('Hello')}")
    print(f"Truthy/Falsy for '' is {check_truthy('')}")
    print(f"Truthy/Falsy for [] is {check_truthy([])}")
    print(f"Truthy/Falsy for [1, 2, 3] is {check_truthy([1, 2, 3])}")


if __name__ == "__main__":
    main()