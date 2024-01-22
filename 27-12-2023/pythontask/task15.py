a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))
c=int(input("Enter 3rd value:"))
if ((a+b>c)==(a+c>b)==(b+c>a)):
    print("The Triangle is valid")
else:
    print("The Triangle is not valid")