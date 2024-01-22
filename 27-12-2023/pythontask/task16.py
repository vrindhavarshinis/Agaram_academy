a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))
c=int(input("Enter 3rd value:"))
if (a==c and a!=b and b!=c)or(a==b and a!=c and c!=b)or(b==c and b!=a and a!=c):
    print("It is an Isoscceles Triangle")
elif(a==b and b==c and c==a ):
    print("It is an Equilateral Triangle")
elif(a!=b and b!=c and c!=a ):
    print("It is a Scalar Triangle")
    