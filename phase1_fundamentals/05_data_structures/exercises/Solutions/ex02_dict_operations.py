def main():
    stud_grad = {"a": 55, "b": 65, "c": 95, "d": 25, "e": 75, "f": 65}
    print("student names range from a to f")

    stud_name = input("enter a student name to check their grade: ")
    grade = stud_grad.get(stud_name)
    if grade is not None:
        print(f"the grade of student {stud_name} is {grade}")
    else:
        print("wrong student name, here is the whole list:")
        for name, g in stud_grad.items():
            print(f"{name}: {g}")

    new_stud_name = input("enter a new student name whose grade you want to change: ")
    try:
        new_stud_grade = int(input("enter a new grade: "))
        stud_grad[new_stud_name] = new_stud_grade
    except ValueError:
        print("invalid grade, skipping update")

    print("Here is the whole list:")
    for name, g in stud_grad.items():
        print(f"{name}: {g}")
    pass


if __name__ == "__main__":
    main()
