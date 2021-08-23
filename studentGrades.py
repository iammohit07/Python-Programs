def get_grade(a, b, c, d):

    per = (a+b+c+d)/400
    per = per*100

    if(per > 80):
        print("GRADE IS - A")
    elif(per < 80 and per > 60):
        print("GRADE IS - B")
    elif(per < 60 and per > 50):
        print(" GRADE IS - C")
    else:
        print("FAIL")


print("ENTER MARKS OF 4 SUBJECTS : ")
a = int(input("MARKS OF SUBJECT 1 : "))
b = int(input("MARKS OF SUBJECT 2 : "))
c = int(input("MARKS OF SUBJECT 3 : "))
d = int(input("MARKS OF SUBJECT 4 : "))
get_grade(a, b, c, d)
