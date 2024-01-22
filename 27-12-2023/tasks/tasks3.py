salary=int(input("Enter your Salary amount:"))
yearofservice=int(input("Enter your Year of service in a company:"))
if yearofservice>5:
    print("Netbonus=",salary*5/100)
else:
    print("No bonus")