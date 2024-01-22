input1=int(input("Enter 1st value:"))
input2=int(input("Enter 2nd value:"))
input3=int(input("Enter 3rd value:"))
total=input1+input2+input3

if total==180:
    print("The Triangle is valid")
elif input1==0 or input2==0 or input3==0:
    print("The Input was not valid for Triangle")
else:
    print("The Triangle is not valid")

