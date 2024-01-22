
physics=int(input("Enter Your Physics Mark:"))
chemistry=int(input("Enter Your Chemistry Mark:"))
biology=int(input("Enter Your Biology Mark:"))
mathematics=int(input("Enter Your Maths Mark:"))
computer=int(input("Enter Your computer Mark:"))

percentage=(physics+chemistry+biology+mathematics+computer)/500*100

if percentage>=90:
    print("Grade A")
elif percentage>=80 and percentage<90:
    print("Grade B")
elif percentage>=70 and percentage<80:
    print("Grade C")
elif percentage>=60 and percentage<70:
    print("Grade D")
elif percentage>=40 and percentage<60:
    print("Grade E")
elif percentage<40 and percentage<40:
    print("Grade F")

