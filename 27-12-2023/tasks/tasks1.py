length=int(input("Enter length value:"))
breadth=int(input("Enter breadth value:"))
if length==breadth:
    print("It is a square")
elif length!=breadth and length<breadth:
    print("It is a rectangle")
else:
    print("It is not a rectangle or square")