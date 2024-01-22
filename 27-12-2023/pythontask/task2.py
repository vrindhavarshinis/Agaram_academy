value_1=int(input("Enter Value 1:"))
value_2=int(input("Enter Value 2:"))
value_3=int(input("Enter Value 3:"))
if value_1>value_2 and value_1>value_3:
    print(value_1, "is Maximum")
elif value_2>value_1 and value_2>value_3:
    print(value_2," is Maximum")
elif value_3>value_1 and value_3>value_2:
    print(value_3,"is Maximum")
elif value_1==value_2 and value_2==value_3 and value_3==value_1:
    print(value_1, value_2, value_3,"All Values are equal")
elif value_1==value_2 and value_2!=value_3 and value_1!=value_3 and (value_1>value_3 and value_2>value_3):
    print(value_1,"and",value_2 ,"are equal and both are maximum" )
elif value_2==value_3 and value_3!=value_1 and value_2!=value_1 and (value_2>value_1 and value_3>value_1):
    print(value_2,"and",value_3, "are equal and both are maximum")
elif value_3==value_1 and value_3!=value_2 and value_1!=value_2 and (value_3>value_2 and value_1>value_2):
    print(value_3,"and",value_1, "are equal and both are maxium")
else:
    print("Invalid")

