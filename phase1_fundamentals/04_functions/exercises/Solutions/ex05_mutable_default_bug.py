def main():
    # ---- BUGGY VERSION ----
    def add_item_buggy(item, my_list=[]):  # mutable default argument!
        my_list.append(item)
        return my_list

    print("BUGGY VERSION:")
    print(add_item_buggy("apple"))   # expect: ['apple']
    print(add_item_buggy("banana"))  # expect: ['banana'], but NOT what happens
    print(add_item_buggy("cherry"))  # expect: ['cherry'], but NOT what happens

    print()

    # ---- FIXED VERSION ----
    def add_item_fixed(item, my_list=None):
        if my_list is None:
            my_list = []  # fresh list created every call
        my_list.append(item)
        return my_list

    print("FIXED VERSION:")
    print(add_item_fixed("apple"))   # ['apple']
    print(add_item_fixed("banana"))  # ['banana']
    print(add_item_fixed("cherry"))  # ['cherry']

if __name__ == "__main__":
    main()