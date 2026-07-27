from itertools import chain, islice


def main():
    iterable_1 = range(10)
    iterable_2 = range(10, -1, -1)

    print("Original Iterables")
    print("------------------")
    print(f"Iterable 1: {list(iterable_1)}")
    print(f"Iterable 2: {list(iterable_2)}")

    # itertools.chain()
    print("\nUsing itertools.chain()")
    print("-----------------------")

    combined = chain(iterable_1, iterable_2)

    # chain() returns a lazy iterator
    print("Chain object:")
    print(combined)

    # Convert to a list to consume the iterator
    combined_list = list(combined)
    print("\nCombined values:")
    print(combined_list)

    # Iterator is now exhausted
    print("\nChain after being consumed:")
    print(list(combined))

    # itertools.islice()
    print("\nUsing itertools.islice()")
    print("------------------------")

    sliced = islice(range(10), 2, 7)

    # islice() also returns a lazy iterator
    print("islice object:")
    print(sliced)

    # Convert to a list to consume the iterator
    sliced_list = list(sliced)
    print("\nSlice from index 2 to 6:")
    print(sliced_list)

    # Iterator is now exhausted
    print("\nislice after being consumed:")
    print(list(sliced))


if __name__ == "__main__":
    main()
