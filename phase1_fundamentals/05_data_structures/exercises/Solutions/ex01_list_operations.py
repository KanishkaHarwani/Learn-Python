def main():
    def show(label, lst):
        print(label)
        print(f"this is the current list: {lst}")
        print("-" * 50)
    main_list = ['a', 'b', 'c', 'd', 'g', 'h', 'i', 'e', 'f', 'j']
    show("initial list", main_list)

    main_list.append('z')
    show("appended z", main_list)

    main_list.insert(5, "q")
    show("insert q at index 5", main_list)

    main_list.remove('f')
    show("remove f from main_list", main_list)

    main_list.sort()
    show("sorted list", main_list)
    pass


if __name__ == "__main__":
    main()
