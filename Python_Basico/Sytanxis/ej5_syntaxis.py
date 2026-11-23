done = False;
grades_number = 0
grades_sum = 0
general_avg = 0
approved_grades = 0 
approved_sum = 0
approved_avg = 0
failed_grades = 0
failed_sum = 0
failed_avg = 0


while not done :
    user_input = (input('Please indicate a grade (type "d" when you are done): '))

    if user_input == "d":
        break

    grade = int(user_input)
    grades_number = grades_number +  1
    grades_sum = grades_sum + grade

    if grade >= 70 :
        approved_grades = approved_grades + 1
        approved_sum = approved_sum + grade 
    else:
        failed_grades = failed_grades + 1
        failed_sum = failed_sum + grade

if grades_number > 0 : 
    general_avg = grades_sum / grades_number

    if approved_grades > 0 :
        approved_avg = approved_sum / approved_grades

    if failed_grades > 0:
        failed_avg = failed_sum / failed_grades 

    print(f"The student grade average is: {general_avg}")
    print(f"The student has {approved_grades} grade(s) approved")
    print(f"The student has {failed_grades} grade(s) failed")
    print(f"The average of approved grades is: {approved_avg}")
    print(f"The average of failed grades is: {failed_avg}")

else:
    print("No grades have been entered")