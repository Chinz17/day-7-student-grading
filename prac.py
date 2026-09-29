print("student grading program")
def get_grade (marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return"B"
    elif marks >= 40:
        return "C"
    else :
        return "fail"

name = input("enter your name : ")
marks = int(input("enter your marks : "))
print(name)
print(get_grade(marks))