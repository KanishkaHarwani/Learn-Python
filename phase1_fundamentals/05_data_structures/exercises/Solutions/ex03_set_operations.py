def main():
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {1, 2, 9, 4, 6}
    print(f"this is set 1: {set_1}")
    print(f"this is set 2: {set_2}")
    union = set_1.union(set_2)
    print(f"union set 1 and set 2: {union}")
    intersection = set_1.intersection(set_2)
    print(f"intersection set 1 and set 2: {intersection}")
    diff_1_2 = set_1.difference(set_2)  # in set_1 but not set_2
    diff_2_1 = set_2.difference(set_1)  # in set_2 but not set_1
    print(f"in set_1 but not set_2: {diff_1_2}")
    print(f"in set_2 but not set_1: {diff_2_1}")
    
if __name__ == "__main__":
    main()
