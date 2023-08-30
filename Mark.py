Subjects = int(input("Enter How many subject you have : "))
Students = int(input("Enter students count : "))
for student in range(Students):
    student_name = input(f"Enter student name {student+1}: ")
    print("Enter marks for ",student_name)
    marks = []
    for subject in range(Subjects):
        mark = int(input(f"enter Marks for Subject {subject+1}"))
        marks.append(mark)
    print("Marks for ",student_name)
    for mark_lst in range(len(marks)):
        print(f"Mark {mark_lst + 1} for Subject {mark_lst +1}are :",marks[mark_lst])    

    

          