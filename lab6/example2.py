grade_list = []



numberStudents = int(input("Please , enter number of students:"))



for i in range(numberStudents):

    print("Student ", str(i+1))

    mid_1 = int(input("You write note of Midterm 1:  "))

    mid_2 = int(input("You write note of Midterm 2:"))

    f_grade = int(input(" You write note of Final:"))

    grade_list.append([mid_1,mid_2,f_grade])



print(grade_list)

avg_grades = []



for sub_grades in grade_list:

    avg_grades.append(sub_grades[0]*0.3 + sub_grades[1]*0.3 + sub_grades[2]*0.4)

print(avg_grades)