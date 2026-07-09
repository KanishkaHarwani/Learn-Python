def first_prime_after(n):
    # TODO: implement using break
    p = n + 1
    check = 0
    while check >= 0:
        check = 0
        for i in range(2, n):
            if  p % i == 0:
                check +=1
        if check == 0:
            return p
        p += 1


def sum_ignoring_negatives(numbers):
    # TODO: implement using continue
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total

def contains_duplicate(items):
    index = 0
    for item in items:
        if item in items[index + 1:]:
            return True
        index += 1
    else:
        return False


if __name__ == "__main__":
    # TODO: test all three functions
    # Testing first_prime_after
    print(first_prime_after(23))

    # Testing sum_ignoring_negative
    numbers = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10]
    print(sum_ignoring_negatives(numbers))

    # Testing Contains_duplicates
    items = [1,2,3,4,5,7,8,7,10]
    print(contains_duplicate(items))
