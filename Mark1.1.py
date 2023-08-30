Subjects = int(input("Enter How many subject you have : "))
Students = int(input("Enter students count : "))
for student in range(Students):
    student_name = input(f"Enter student name {student+1}: ")
    print("Enter marks for ",student_name)
    marks = []
    for subject in range(Subjects):
        mark = int(input(f"enter Marks for Subject {subject+1}"))
        marks.append(mark)        
    print(f"{student_name}'s,Marks for Subject are :",marks)    
