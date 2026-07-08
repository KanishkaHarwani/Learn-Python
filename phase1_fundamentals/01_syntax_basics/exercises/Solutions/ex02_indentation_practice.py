def main():
    num = int(input("enter a number less than hundred:"))
    if num < 100:
        print(f"the number {num} is less than 100 ")
        if num % 2 == 0:
            print(f"{num} is even ")
        else:
            print(f"{num} is odd ")
    else:
        print(f"the number {num} is more than 100 and is an invalid input")
    pass


if __name__ == "__main__":
    main()
