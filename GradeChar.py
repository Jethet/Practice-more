# Change numeric grade into letter equivalent

def grade_equivalent():
    grade = float(input("Please enter your grade: "))
    grade_list = {4:'A+', 3.7:'A-', 3:'B',2.7 :'B-'}
    if grade > 4.0:
        print("Your grade point should be 4.0 or less.")
    elif grade not in grade_list:
        print("This is not a valid grade point. Please enter a positive number.")
    else:
        print(grade_list.get(grade))

grade_equivalent()
