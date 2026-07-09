def sum_of_multiples(limit, list):
    # TODO: implement using a for loop over range(limit)
    sum = 0
    for n in range(limit):
        for i in list:
            if n % i == 0:
                sum += n
                break
    return sum

def first_n_squares(n):
    # TODO: implement using a for loop
    for i in range(n):
        print(f"{i ** 2} \n")


if __name__ == "__main__":
    # TODO: test both functions and print results
    lim = 25
    lt = [2, 3]
    n = 10
    print(f"sum of multiples: \n {sum_of_multiples(lim, lt)}")
    print(f"First n squares: \n "
          f"{first_n_squares(n)}")

    pass
