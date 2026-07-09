def classify_number(n):
    # TODO: implement using if / elif / else
    if n < 0:
        print(f"{n} is negative!")
    elif n == 0:
        print(f"{n} is zero!")
    elif n > 0 and n <= 10:
        print(f"{n} is Small and positive!")
    else:
        print(f"{n} is Large and positive!")

if __name__ == "__main__":
    # TODO: test classify_number with a few values, e.g. -5, 0, 4, 25
    values = [-5, 0, 4, 25]
    for val in values:
        classify_number(val)
    pass
