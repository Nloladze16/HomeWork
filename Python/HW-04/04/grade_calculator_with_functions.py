def main():
    grade = int(input("Enter your score: "))

    letter = get_letter_grade(grade)

    print(f"Grade: {letter}")

    passing = is_passing(grade)

    if passing == True:
        print(f"Passing: Yes")
    else:
        print(f"Passing: No")

    print(get_grade_message(grade))    


def get_letter_grade(n):

    if n <= 100 and n >= 90:
        return "A"
    elif n < 90 and n >= 80:
        return "B"
    elif n < 80 and n >= 70:
        return "C"
    elif n < 70 and n >= 60:
        return "D"
    else:
        return "F"


def is_passing(score):
    return score >= 60


def get_grade_message(score):
    if score >= 90:
        return "Excellent work!"
    elif score >= 80:
        return "Good job!"
    elif score >= 70 :
        return "Satisfactory performance."
    elif score >= 60 :
        return "Needs improvement, but passing."
    else :
        return "Failing grade. Please study harder."

if __name__ == "__main__":
    main()


# 90-100: A -> Excellent work!
# 80-89 : B -> Good job!
# 70-79 : C -> Satisfactory performance.
# 60-69 : D -> Needs improvement, but passing.
# Below 60: F -> Failing grade. Please study harder.
