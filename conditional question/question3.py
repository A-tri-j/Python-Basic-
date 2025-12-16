score=int(input("Give me score : "))


if score>= 101:
    print ("Plese verify your score again ")
    exit()
if score>=90:
    grade= "A"
elif score >=80:
    grade="B"
elif score >=70:
    grade="C"
elif score >=60:
    grade="c"
else:
    grade="F"

print("Grade = " ,grade)