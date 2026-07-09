def grade_and_honors(score):
    # TODO: implement with nested if statements
    # Grades: "A"(90+), "B"(80-89), "C"(70-79), "D"(60-69), "F"(<60>)
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    # TODO: test with scores like 97, 91, 82, 55
    scores = [97, 91, 82, 55]
    for score in scores:
        print(grade_and_honors(score))
    pass
