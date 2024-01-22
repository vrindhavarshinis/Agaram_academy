student_details=[
    {
       " name":(input("Enter Your Name:")),
        "age":int(input("Enter your Age:"))
    },
    {
        "name":(input("Enter Your Name 1:")),
        "age":int(input("Enter Your Age 1:"))
    },
    {
        "name":(input("Enter Your Name 2:")),
        "age":int(input("Enter Your Age 2:"))
    }
]
print(student_details[2]["name"])