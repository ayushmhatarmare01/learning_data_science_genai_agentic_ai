#Input the studen name
# #Input marks in five subjects.
#Each mark must be between 0 and 100.
# If any mark is invalid, print an error. 
# Otherwise, if any subject is below 35, the student fails.
# If all subjects are passed,
#  assign a grade using average: A ≥ 90, B ≥ 75, C ≥ 60, otherwise D
name=input("Enter the Name :")
math=int(input("Enter math marks: "))
science=int(input("Enter science marks: "))
hindi=int(input("Enter hindi marks: "))
if (math<0 or math>100 or hindi<0 or hindi>100 or science<0 or science>100):
    print("Invalid marks Enter marks between 0 and 100.")
else:
    total=science+math+hindi
    average=total/3
    print("Name:",name)
    print("Total:",total)
    print("Average:",average)
    if math >= 35 and science >= 35 and hindi >= 35:
        print("Result: Pass")
        if average>=90:
            print("Grade: A")
        elif average>=75:
            print("Grade: B")
        elif average>=60:
            print("Grade: C")
        elif average>=40:
            print("Grade: D")
        else:
            print("Grade: F")
    else:
        print("Result: Fail")