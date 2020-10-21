"""You are tasked to ask the user for 2 values, 2 different grades from semester 1 and semester 2, and you need to calculate the average as well as determine whether they got an A, B, C, or if they failed. Download the template or you may create your own file.

A = 90 and above

B = between 80 and 89

C = between 70 and 79

failing is below 70 (not including 70, 70 is a passing score)"""

name = input("Enter your Name ==>")

sem1 = int(input("Enter your score for Semester1==>"))
sem2 = int(input("Enter your score for Semester2==>"))

avgscore = ((sem1+sem2)/2)

if avgscore >=70 and avgscore<80:
    print(name+" - Congratulations!!! You have passed with Grade C")
elif avgscore >=80 and avgscore<90:
    print(name+" - Congratulations!!! You have passed with Grade B")
elif avgscore >=90:
    print(name+" - Congratulations!!! You have passed with Grade A")
else:
    print (name+" - Unfortunately you have Failed, better luck next time!!!")
