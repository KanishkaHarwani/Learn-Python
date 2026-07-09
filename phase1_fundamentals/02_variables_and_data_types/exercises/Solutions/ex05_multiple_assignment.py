def main():
    a = 5
    b = 10

    print("Before swap:")
    print(f"a = {a}")
    print(f"b = {b}")

    a, b = b, a

    print("\nAfter swap:")
    print(f"a = {a}")
    print(f"b = {b}")

    person = ("John", 28, "Engineer")

    name, age, occupation = person

    print("\nPerson Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Occupation: {occupation}")

    num1 = int(input("\nEnter the first number: "))
    num2 = int(input("Enter the second number: "))

    num1, num2 = num2, num1

    print("\nAfter swapping:")
    print(f"First number: {num1}")
    print(f"Second number: {num2}")
    pass


if __name__ == "__main__":
    main()
