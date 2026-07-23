def main():
    school_dict = [
        {"Name": "Kanishka", "Age": 27, "Grade": 98},
        {"Name": "Hari", "Age": 22, "Grade": 70},
        {"Name": "Sakshi", "Age": 24, "Grade": 82},
        {"Name": "Piyush", "Age": 21, "Grade": 75},
        {"Name": "Kashish", "Age": 23, "Grade": 65},
        {"Name": "Tanmay", "Age": 21, "Grade": 55},
        {"Name": "Mayan", "Age": 21, "Grade": 82},
        {"Name": "Pankaj", "Age": 22, "Grade": 45},
        {"Name": "Vipul", "Age": 24, "Grade": 55}
    ]
    for student in school_dict:
        print(f"name: {student['Name']}, Age: {student['Age']}, Grade - {student['Grade']}")


if __name__ == "__main__":
    main()
