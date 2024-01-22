import math
a=int(input("Enter the 1st co-efficient of equation:"))
b=int(input("Enter the 2nd co-efficient of equation:"))
c=int(input("Enter the 3rd co-efficient of equation:"))
d=(b**2)-(4*a*c)
d1=d**0.5

root_1=(-b+d1)/2*a
root_2=(+b+d1)/2*a

print("Root1=",root_1,"Root2=",root_2)

# if d==0:
#     print( root_1, "and" ,root_2," Roots are real and equal")
# elif d>0 :
#     print( root_1, "and" ,root_2," Roots are real and not equal")
# elif d<0:
#     print("The Roots are imaginary")